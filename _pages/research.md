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


Working Papers
------

* **Inference for Large-Dimensional Panel Data with Many Covariates** [(Paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) [(Code)](https://github.com/jiachzou/panel_multiple_testing). Co-author: Pelger M.
    - We propose Panel Multiple Testing that allows us to select covariates that explain a large cross-section with false discovery control. Empirically, we select sparse risk factors from a factor zoo of 114, to explain 243 doubly-sorted portfolio excess returns. 
    - NASMES 2023, AMES 2023, INFORMS 2023, 11th Western Conference on Mathematical Finance, NBER-NSF SBIES 2022, California Econometrics Conference 2022
	- Featured in Stanford HAI [Financial Services Industry Review](https://hai.stanford.edu/industry-brief-financial-services-and-ai)

* **Large Dimensional Change Point Detection with FWER Control as Automatic Stopping** [(Poster)](https://drive.google.com/file/d/14xcom92GMaCcFZpjLXblOc4K5FlCr6rP/view?usp=sharing) [(Code)](https://github.com/yfan7/panel_CPD). Co-author: Fan Y., Pelger M.
    - With hundreds of time series to detect unknown number of change points, our statistical inference based method is better suited than classical DP-based algorithm. On the theoratical front, we provide FWER control. In simulations, we showed 20% lift in F1 scores against leading benchmarks.
    - ICML 2023 Workshop on Structured Probabilistic Inference & Generative Modeling

* **Improving Deceased Donor Kidney Allocation with Machine Learning**<br>
	Co-authors: Agarwal N, Ashlagi I, Guan G, Somaini P.<br>
	- In this paper, we leverage geographical and temporal information to identify at-risk cadaveric kindeys. We use machine learning to construct a novel risk score as the predicted probability of hard-to-place, and performed extensive analysis on the medical reasons why the algorithm makes mistakes.
    - NeurIPS 2022 TS4H, INFORMS 2022


Work in Progress
------
* **Learning Bipartite Relationship Graph with Applications for National Kidney Allocation Policy Evaluations**. Co-author: Ugander J., Ashlagi I.
    - We propose new method that learns relationship graph from longitudinal observation of nodes interactions. The learned graph has Type I error control on falsely discovered edge, using Panel Multiple Testing.