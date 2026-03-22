---
title: "Graph Machine Learning for Asset Pricing: Traversing the Supply Chain"
collection: publications
permalink: /research/gnn-supply-chain-pricing/
date: 2024-11-01
venue: "Journal of Financial Economics"
status: "Major Revision"
authors: "Agostino Capponi, Jose Sidaoui, Jiacheng Zou"
paperurl: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617"
codeurl: "https://github.com/agcappo/SupplyChainAssetPricing"
thumbnail: /images/blog/gnn-supply-chain-pricing-thumb.png
---

<div style="display:inline-block; background:#1a5276; color:#fff; font-size:0.78rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; padding:0.35em 0.9em; border-radius:3px; margin-bottom:1.5rem;">
  Major Revision &nbsp;·&nbsp; Journal of Financial Economics
</div>

<div style="display:flex; gap:1rem; margin-bottom:2rem; flex-wrap:wrap;">
  <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617" class="btn btn--primary" target="_blank" rel="noopener">Paper (SSRN)</a>
  <a href="https://github.com/agcappo/SupplyChainAssetPricing" class="btn" target="_blank" rel="noopener">Code</a>
</div>

<figure style="float:right; margin: 0 0 1.5rem 2rem; max-width:340px;">
  <img src="/images/blog/gnn-supply-chain-pricing-thumb.png"
       alt="GNN supply chain comic thumbnail"
       style="width:100%; border-radius:6px; border:1px solid #e0e0e0; box-shadow:0 2px 12px rgba(0,0,0,0.08);">
</figure>

## Abstract

We develop a nonparametric method to aggregate firm characteristics across a large supply chain network to explain cross-sectional expected returns. Each firm receives a pricing signal, nonlinearly constructed from the characteristics of neighboring firms within $d$-hops on the network. We find that $d = 3$ — encompassing network effects up to the third order — balances bias reduction from higher-order relations against variance from added complexity.

Our model leads to a portfolio sorted by ML-driven firm-level estimated returns that condition on both historical supply chain data and firm characteristics. We achieve over a **16% out-of-sample Sharpe gain** versus direct-link models, and outperform the Fama–French five-factor and PCA benchmarks. We find that the ML-managed portfolio improves mean-variance efficiency, measured by Sharpe ratio. Lastly, we show that the conditional mean return estimation of more **central firms** is 55% more sensitive to missingness of supply chain links compared to that of peripheral firms in the supply chain graph.

## Key Contributions

- A graph attention network (GNN) that aggregates firm characteristics up to $d$ hops along supplier–customer edges, with data-driven depth selection
- Formal characterization of the **bias–variance tradeoff** in higher-order neighborhood aggregation for return prediction
- An empirical asset pricing study showing that supply chain topology contains return-predictive information invisible to linear factor models
- A centrality-based guide for supply chain data quality investment

## Presentations

UT Austin, UNC, Baruch; SoFiE, NFA, EFA, Inaugural Finance Research Revolution Conference (Vitznau, Switzerland), INFORMS, Luohan Academy

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: { inlineMath: [['$','$'], ['\\(','\\)']], processEscapes: true }
  });
</script>
