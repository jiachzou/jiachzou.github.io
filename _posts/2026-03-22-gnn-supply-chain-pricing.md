---
layout: blog-post
title: 'Graph ML for Asset Pricing: Traversing the Supply Chain'
date: 2026-03-22
authors: Agostino Capponi, Jose Sidaoui, Jiacheng Zou
tldr: Firms don't live in isolation — their stock returns depend on who they buy from
  and sell to. We build a Graph Neural Network that propagates firm characteristics
  up to 3 hops along the supply chain, achieving 16%+ out-of-sample Sharpe ratio gains
  over direct-link models and beating Fama-French five-factor benchmarks.
thumbnail: /images/blog/gnn-supply-chain-pricing-thumb.png
categories: research
tags:
- GNN
- asset pricing
- supply chain
- machine learning
---

Standard asset pricing treats firms as isolated atoms — each valued solely on its own balance sheet, momentum, and factor loadings. But in reality, a chip shortage at TSMC reverberates through Apple's supply chain, and on to every automaker waiting for electronics. **Why should we expect a model that ignores these connections to price assets well?**

We don't — and in this paper, we show that it can't.

---

## The Idea

We construct a supply chain graph where each node is a publicly traded firm and each edge is a reported supplier-customer relationship. Instead of pricing firms independently, we train a **Graph Attention Network (GNN)** that aggregates characteristics from a firm's neighbors — and their neighbors' neighbors — to build a richer pricing signal.

The key question: *how far should the model look?* A tier-1 supplier shock matters for an automaker. Does a tier-3 shock? We let the data answer: the optimal depth is **$d = 3$ hops**, balancing the bias reduction from capturing higher-order linkages against the noise introduced by more distant, weaker connections.

---

## Key Results

- **+16% out-of-sample Sharpe ratio** vs. direct-link ($d=1$) models
- Outperforms the **Fama–French five-factor** and **PCA** benchmarks
- The ML-managed long–short portfolio improves **mean-variance efficiency** relative to standard factor models
- **Central firms** (high eigenvector centrality) are **55% more sensitive** to missing supply chain links than peripheral firms — a practical guide for where data quality investment pays off most

---

## Why It Matters

Supply chain data has become increasingly available and granular. This paper shows it contains return-predictive information that is *nonlinearly* entangled with firm characteristics — invisible to linear factor models, but learnable by a well-designed GNN. The attention mechanism further reveals which upstream and downstream relationships are doing the pricing work, providing economic interpretability alongside predictive power.

---

<div style="margin: 2rem 0; padding: 1.25rem 1.5rem; border: 1px solid #e0e0e0; border-radius: 6px; background: #fafafa;">
  <p style="margin:0 0 0.75rem 0; font-size:0.85rem; color:#555; font-weight:600; text-transform:uppercase; letter-spacing:0.06em;">Read the full paper</p>
  <p style="margin:0 0 0.5rem 0;">
    <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617" target="_blank" rel="noopener" style="font-size:1rem; font-weight:700; color:#1a5276;">
      Graph Machine Learning for Asset Pricing: Traversing the Supply Chain →
    </a>
  </p>
  <p style="margin:0; font-size:0.83rem; color:#777;">
    Capponi, Sidaoui &amp; Zou &nbsp;·&nbsp; SSRN Working Paper 5031617
  </p>
  <p style="margin:0.6rem 0 0 0; font-size:0.83rem;">
    <a href="https://github.com/agcappo/SupplyChainAssetPricing" target="_blank" rel="noopener">Code on GitHub</a>
  </p>
</div>
