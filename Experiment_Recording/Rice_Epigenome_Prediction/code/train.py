import os
import torch
import torch.nn as nn
import time
from Functions import *
from Dataset import *
from Network import *
from LrScheduler import *
import Metrics
from Logger import CSVLogger
import argparse
from tensorboardX import SummaryWriter
from torch.cuda.amp import autocast as autocast
from torch.cuda.amp import GradScaler as GradScaler



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu_id', type=str, default='0',  help='which gpu to use')
    parser.add_argument('--path', type=str, default='../', help='path of csv file with DNA sequences and labels')
    parser.add_argument('--epochs', type=int, default=150, help='number of epochs to train')
    parser.add_argument('--batch_size', type=int, default=24, help='size of each batch during training')
    parser.add_argument('--weight_decay', type=float, default=0, help='weight dacay used in optimizer')
    parser.add_argument('--ntoken', type=int, default=4, help='number of tokens to represent DNA nucleotides (should always be 4)')
    parser.add_argument('--nclass', type=int, default=2, help='number of classes from the linear decoder')
    parser.add_argument('--ninp', type=int, default=512, help='ninp for transformer encoder')
    parser.add_argument('--nhead', type=int, default=8, help='nhead for transformer encoder')
    parser.add_argument('--nhid', type=int, default=2048, help='nhid for transformer encoder')
    parser.add_argument('--nlayers', type=int, default=6, help='nlayers for transformer encoder')
    parser.add_argument('--save_freq', type=int, default=1, help='saving checkpoints per save_freq epochs')
    parser.add_argument('--dropout', type=float, default=.1, help='transformer dropout')
    parser.add_argument('--warmup_steps', type=int, default=3200, help='training schedule warmup steps')
    parser.add_argument('--lr_scale', type=float, default=0.1, help='learning rate scale')
    parser.add_argument('--kmers', type=int, nargs='+', default=[2,3,4,5,6], help='k-mers to be aggregated')
    #parser.add_argument('--kmer_aggregation', type=bool, default=True, help='k-mers to be aggregated')
    parser.add_argument('--kmer_aggregation', dest='kmer_aggregation', action='store_true')
    parser.add_argument('--no_kmer_aggregation', dest='kmer_aggregation', action='store_false')
    parser.set_defaults(kmer_aggregation=True)
    parser.add_argument('--nfolds', type=int, default=5, help='number of cross validation folds')
    parser.add_argument('--fold', type=int, default=0, help='which fold to train')
    parser.add_argument('--val_freq', type=int, default=1, help='which fold to train')
    parser.add_argument('--num_workers', type=int, default=1, help='num_workers')
    parser.add_argument('--record',  type=str, default=' ', help='train or test record')
    opts = parser.parse_args()
    return opts

tb = SummaryWriter('/root/my_train/tblogdir/H3K4me3_final')

def train_fold():

    opts = get_args()
    seed_everything(2020)
    #gpu selection
    os.environ["CUDA_VISIBLE_DEVICES"] = opts.gpu_id
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data = pd.read_csv('/root/my_train/dataset_all/H3K4me3_train_45w.txt', header=None,  sep='\t')

    dataset = ViraminerDataset(data.iloc[:410000,0],data.iloc[:410000,1])
    dataloader = torch.utils.data.DataLoader(dataset,batch_size=opts.batch_size,shuffle=True,num_workers=opts.num_workers)
    val_dataset = ViraminerDataset(data.iloc[410000:,0],data.iloc[410000:,1])
    val_dataloader = torch.utils.data.DataLoader(val_dataset,batch_size=opts.batch_size,shuffle=False)

    #exit()
    #lr=0

    #checkpointing
    checkpoints_folder = '{}checkpoints_fold{}'.format(opts.record, opts.fold)
    csv_file = '{}log_fold{}.csv'.format(opts.record, opts.fold)
    columns = ['epoch','train_loss',
             'val_loss','val_auc','val_acc','val_sens','val_spec']
    logger = CSVLogger(columns,csv_file)

    #build model and logger
    model = NucleicTransformer(opts.ntoken, opts.nclass, opts.ninp, opts.nhead, opts.nhid,
                           opts.nlayers, opts.kmer_aggregation, kmers=opts.kmers,
                           dropout=opts.dropout).to(device)
    optimizer = torch.optim.Adam(model.parameters(), weight_decay=opts.weight_decay)
    criterion = nn.CrossEntropyLoss(reduction='none')
    lr_schedule = lr_AIAYN(optimizer,opts.ninp,opts.warmup_steps,opts.lr_scale)
    
    softmax = nn.Softmax(dim=1)
    
    pytorch_total_params = sum(p.numel() for p in model.parameters())
    print('Total number of paramters: {}'.format(pytorch_total_params))

    print("Starting training for fold {}/{}".format(opts.fold,opts.nfolds))
    #training loop
    scaler = GradScaler()
    for epoch in range(opts.epochs):
        model.train(True)
        t = time.time()
        total_loss = 0
        total_steps = len(dataloader)
        for step, data in enumerate(dataloader):
        #for step in range(1):
            lr = lr_schedule.step()
            src = data['data'].to(device)
            labels = data['labels'].to(device)
            optimizer.zero_grad()

            with autocast():
            	output = model(src)
            	loss = torch.mean(criterion(output,labels))
            
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(),1)
            scaler.step(optimizer)
            scaler.update()
            
            total_loss += loss

            print ("Epoch [{}/{}], Step [{}/{}] Loss: {:.3f} Lr:{:.6f} Time: {:.1f}"
                           .format(epoch+1, opts.epochs, step+1, total_steps, total_loss/(step+1) , lr,time.time()-t),end='\r',flush=True) #total_loss/(step+1)
            #break
        print('')

        train_loss = total_loss/(step+1)        

        if (epoch+1)%opts.val_freq == 0:
            val_loss,auc,val_acc,val_sens,val_spec=validate(model,device,val_dataloader,batch_size=opts.batch_size*2)
            print("Epoch {} train loss: {}".format(epoch+1,train_loss))
            tb.add_scalars('train/val/loss', {'train':train_loss, 'val':val_loss}, epoch+1)
            tb.add_scalar('val_acc', val_acc, epoch+1)
            tb.add_scalar('auc', auc, epoch+1)
            tb.add_scalar('val_sens', val_sens, epoch+1)
            tb.add_scalar('val_spec', val_spec, epoch+1)

            to_log = [epoch+1,train_loss,val_loss,auc,val_acc,val_sens,val_spec]
            logger.log(to_log)
            

        if (epoch+1)%opts.save_freq == 0:
            save_weights(model,optimizer,epoch,checkpoints_folder)
    
    tb.close()
    get_best_weights_from_fold(opts.record, opts.fold)
    
train_fold()
