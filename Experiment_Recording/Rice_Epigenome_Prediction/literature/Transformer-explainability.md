# Transformer Interpretability Beyond Attention Visualization
## Abstract
A novel way to compute relevancy for Transformer Network.
The methods assigns local relevance based on the Deep Taylor Decomposition principle and the propagates these relevancy scores through the layers.
The solution is based on a specific formulation that is shown to maintain the total relevancy across layers.
## Introduction
### why visualization?
help debugging,verify model is fair and unbiased, and enable downstream.
Self-attention Layers assign a pairwise attention value between every two tokens.
### A common ways:
for a single layer:Consider these attentions as a relevancy scores 
for multiple layers:Simply averaging the attentions obtained for each token,shortcoming: blurring of the signal and not consider the different role of layers:deeper layers are more semantic, but each token accumulates additional context each time self-attention is applied.
### The rollout method
reassigns all attention scores by considering the pairwise attentions and assuming that attentions are combined linearly into subsequent contexts.
seems to improve results over the utilization of a single attention layer.but by relying simplistic assumptions, irrelevant tokens often become highlighted.
