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

I work on machine learning (ML) aided decision making with 2 streams of research:<br>
<span class="tag-panel-data" style="background-color: rgb(140, 21, 21);  color: white; padding: 2px 5px;">(I) Statistical learning of large panel data</span> and <span class="tag-healthcare" style="background-color: #228B22; color: white; padding: 2px 5px;">(II) Improving healthcare with ML</span>

Roadmap: Paper 1 is foundational and identifies a new class of multiple testing problems in <span class="tag-panel-data" style="background-color: rgb(140, 21, 21);  color: white; padding: 2px 5px;">(I) Statistical learning of large panel data</span> . Papers 2 and 3 are extensions and applications of Paper 1.

------

1. **Inference for Large-Dimensional Panel Data with Many Covariates** [(Paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) [(Code)](https://github.com/jiachzou/panel_multiple_testing) [(Slides)](https://drive.google.com/file/d/14fSXYmFJxZBjXuSz0eOscAtF8ggx1ugg/view?usp=share_link) <br>
	<span class="tag-panel-data" style="background-color: rgb(140, 21, 21);  color: white; padding: 2px 5px;">(I) Statistical learning of large panel data</span>  Co-author: Markus Pelger <br>
    - We propose Panel Multiple Testing that allows us to select covariates that explain a large cross-section with false discovery control. In our empirical asset pricing study, we select sparse risk factors from a factor zoo of 114, to explain 243 doubly-sorted portfolio excess returns. 
    - NASMES 2023, AMES 2023, INFORMS 2023, 11th Western Conference on Mathematical Finance, NBER-NSF SBIES 2022, California Econometrics Conference 2022, Stanford HAI [Financial Services Industry Review](https://hai.stanford.edu/industry-brief-financial-services-and-ai)

2. **Learning Bipartite Relationship Graph with Applications for National Kidney Allocation Policy Evaluations** <br>
    <span class="tag-panel-data" style="background-color: rgb(140, 21, 21);  color: white; padding: 2px 5px;">(I) Statistical learning of large panel data</span>  <span class="tag-healthcare" style="background-color: #228B22; color: white; padding: 2px 5px;">(II) Improving healthcare with ML</span> Co-authors: Johan Ugander, Itai Ashlagi <br>
    - Does exchange occur due to supply-demand relationship, beyond consideration of quality on _two-sided platforms_?  We use the potential outcome framework from causal inference to define dyadic relationships. Leveraging repeated observations of interactions in the platform to construct supplier fixed effects, we propose a multiple testing method to adjust for platform size and control for false discoveries. We study the US deceased donor kidney allocation system by analyzing acceptance decisions from 65 Transplant Centers. The learned relationship graph between Transplant Centers and Organ Procurers provides new information that can help explain the acceptance rate differences across the country, even after we use machine learning to control for medical, logistical, and patient priority contexts. <br>
	 (Draft available upon request)

3. **Large Dimensional Change Point Detection with FWER Control as Automatic Stopping** [(Paper)](https://drive.google.com/file/d/15SotyMqpWBUTrwaCpzNGron2F4uz1wdL/view?usp=sharing) [(Poster)](https://drive.google.com/file/d/14xcom92GMaCcFZpjLXblOc4K5FlCr6rP/view?usp=sharing) [(Code)](https://github.com/yfan7/panel_CPD) <br>
	<span class="tag-panel-data" style="background-color: rgb(140, 21, 21);  color: white; padding: 2px 5px;">(I) Statistical learning of large panel data</span>  Co-authors: Yang Fan, Markus Pelger <br>
    - With hundreds of time series and unknown number of change points to detect, our inference-based method is better suited than the classical DP-based algorithm due to its conscientious trade-off of Type I vs Type II error. We provide FWER control theory. In simulations, we showed 20% lift in F1 scores against leading benchmarks.
    - ICML 2023 [SPIGM](https://spigmworkshop.github.io/), [SCIS](https://sites.google.com/view/scis-workshop-23/accepted-papers?authuser=0)

4. **Improving Deceased Donor Kidney Allocation with Machine Learning**<br>
    <span class="tag-healthcare" style="background-color: #228B22; color: white; padding: 2px 5px;">(II) Improving healthcare with ML</span> Co-authors: Nikhil Agarwal, Itai Ashlagi, Grace Guan, Paulo Somaini<br>
    - In this paper, we leverage geographical and temporal information to identify at-risk cadaveric kidneys. We use machine learning to construct a novel risk score as the predicted probability of hard-to-place, and perform extensive analysis on the medical reasons why the algorithm makes mistakes.
    - NeurIPS 2022 TS4H (Under title _Time-constrained decision making in deceased donor kidney allocation_), INFORMS 2022


<style>
/* Define an animation for the highlighting */
@keyframes highlight {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
}

.tag-panel-data:hover, .tag-healthcare:hover {
    animation: highlight 1s infinite; /* Apply the animation on hover */
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Function to highlight similar tags
    function highlightSimilarTags(tagClass) {
        let tags = document.querySelectorAll('.' + tagClass);
        tags.forEach(tag => {
            tag.style.animation = 'highlight 1s infinite';
        });
    }

    // Function to remove highlighting from tags
    function removeHighlight(tagClass) {
        let tags = document.querySelectorAll('.' + tagClass);
        tags.forEach(tag => {
            tag.style.animation = '';
        });
    }

    // Add event listeners for the tags
    let panelDataTags = document.querySelectorAll('.tag-panel-data');
    panelDataTags.forEach(tag => {
        tag.addEventListener('mouseover', () => highlightSimilarTags('tag-panel-data'));
        tag.addEventListener('mouseout', () => removeHighlight('tag-panel-data'));
    });

    let healthcareTags = document.querySelectorAll('.tag-healthcare');
    healthcareTags.forEach(tag => {
        tag.addEventListener('mouseover', () => highlightSimilarTags('tag-healthcare'));
        tag.addEventListener('mouseout', () => removeHighlight('tag-healthcare'));
    });
});
</script>
