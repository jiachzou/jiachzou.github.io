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

* **Inference for Large-Dimensional Panel Data with Many Covariates** [(Paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) [(Code)](https://github.com/jiachzou/panel_multiple_testing) <br>
    Co-author: Markus Pelger <br>
    - We propose Panel Multiple Testing that allows us to select covariates that explain a large cross-section with false discovery control. In our empirical asset pricing study, we select sparse risk factors from a factor zoo of 114, to explain 243 doubly-sorted portfolio excess returns. 
    - NASMES 2023, AMES 2023, INFORMS 2023, 11th Western Conference on Mathematical Finance, NBER-NSF SBIES 2022, California Econometrics Conference 2022, Stanford HAI [Financial Services Industry Review](https://hai.stanford.edu/industry-brief-financial-services-and-ai)

* **Large Dimensional Change Point Detection with FWER Control as Automatic Stopping** [(Paper)](https://drive.google.com/file/d/15SotyMqpWBUTrwaCpzNGron2F4uz1wdL/view?usp=sharing) [(Poster)](https://drive.google.com/file/d/14xcom92GMaCcFZpjLXblOc4K5FlCr6rP/view?usp=sharing) [(Code)](https://github.com/yfan7/panel_CPD) <br>
    Co-authors: Yang Fan, Markus Pelger <br>
    - With hundreds of time series and unknown number of change points to detect, our inference-based method is better suited than the classical DP-based algorithm due to its conscientious trade-off of Type I vs Type II error. We provide FWER control theory. In simulations, we showed 20% lift in F1 scores against leading benchmarks.
    - ICML 2023 [SPIGM](https://spigmworkshop.github.io/), [SCIS](https://sites.google.com/view/scis-workshop-23)

* **Improving Deceased Donor Kidney Allocation with Machine Learning**<br>
	Co-authors: Nikhil Agarwal, Itai Ashlagi, Grace Guan, Paulo Somaini<br>
	- In this paper, we leverage geographical and temporal information to identify at-risk cadaveric kidneys. We use machine learning to construct a novel risk score as the predicted probability of hard-to-place, and perform extensive analysis on the medical reasons why the algorithm makes mistakes.
    - NeurIPS 2022 TS4H, INFORMS 2022


Work in Progress
------
* **Learning Bipartite Relationship Graph with Applications for National Kidney Allocation Policy Evaluations** <br>
    Co-authors: Johan Ugander, Itai Ashlagi <br>
    - We propose a novel learning framework that identifies relationship graphs from longitudinal observation of node interactions. The learned graph has Type I error control on falsely discovered edges, achieved through Panel Multiple Testing and allows arbitrary covariance of dyadic behavior. We study the national kidney allocation system by building decision models for >70 transplantation hospitals.
