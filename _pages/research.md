---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- Your content here -->


------

1. **Selective Multiple Testing: Inference for Large Panels with Many Covariates** [(Paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) [(Code)](https://github.com/jiachzou/panel_multiple_testing) [(Slides)](https://drive.google.com/file/d/14fSXYmFJxZBjXuSz0eOscAtF8ggx1ugg/view?usp=share_link) <br>
	Co-author: Markus Pelger <br>
    - _R&R at Management Science_.
    - We propose Panel Multiple Testing that allows us to select covariates that explain a large cross-section with false discovery control. In our empirical asset pricing study, we select sparse risk factors from a factor zoo of 114, to explain 243 doubly-sorted portfolio excess returns. 
    - NASMES 2023, AMES 2023, INFORMS 2023, 11th Western Conference on Mathematical Finance, NBER-NSF SBIES 2022, California Econometrics Conference 2022, Stanford HAI [Financial Services Industry Review](https://hai.stanford.edu/industry-brief-financial-services-and-ai)


2. **Large Dimensional Change Point Detection with FWER Control as Automatic Stopping** [(Paper)](https://drive.google.com/file/d/15SotyMqpWBUTrwaCpzNGron2F4uz1wdL/view?usp=sharing) [(Poster)](https://drive.google.com/file/d/14xcom92GMaCcFZpjLXblOc4K5FlCr6rP/view?usp=sharing) [(Code)](https://github.com/yfan7/panel_CPD) <br>
	Co-authors: Yang Fan, Markus Pelger <br>
    - With hundreds of time series and unknown number of change points to detect, our inference-based method is better suited than the classical DP-based algorithm due to its conscientious trade-off of Type I vs Type II error. We provide FWER control theory. In simulations, we showed 20% lift in F1 scores against leading benchmarks.
    - ICML 2023 [SPIGM](https://spigmworkshop.github.io/), [SCIS](https://sites.google.com/view/scis-workshop-23/accepted-papers?authuser=0)

3. **Inference for Large Panel Data with Machine Learning** [(Paper)](https://searchworks.stanford.edu/view/in00000163521) <br>
 - This is my PhD thesis, accessible from Stanford's archival system.


4. **Asset pricing with Supply Chain Relationships** [(Paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617) [(Code)](https://github.com/agcappo/SupplyChainAssetPricing) <br>
	Co-authors: Agostino Capponi, Jose Sidaoui <br>
  - We propose a nonparametric method to aggregate rich firm characteristics over a large supply chain network to explain the cross-section of expected returns. Each target firm receives a nonlinearly constructed pricing signal passed from neighboring firms that are within $d$-hops on the supply chain network. We find supply chain is useful for asset pricing: our model achieves over 50% higher out-of-sample Sharpe ratios compared to models using only direct suppliers and consumers, outperforming Fama-French five-factor and principal component models. Through a graph-Monte Carlo experiment, we demonstrate the interplay between $d$ and degree centrality, showing that the most central firms are twice as sensitive as peripheral firms. Our recommended $d = 6$ balances bias-variance and ensures robustness.
  - INFORMS 2024
    
<!-- Linking CSS and JS -->
<link rel="stylesheet" href="{{ '/assets/css/tags_highlight.css' | relative_url }}">
<script src="{{ '/assets/js/tags_highlight.js' | relative_url }}"></script>
