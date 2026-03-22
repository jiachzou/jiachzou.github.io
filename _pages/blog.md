---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/blog.css' | relative_url }}">

<div class="blog-list">
{% assign posts = site.posts | sort: 'date' | reverse %}
{% if posts.size == 0 %}
  <p>No posts yet. Check back soon.</p>
{% else %}
{% for post in posts %}
  <div class="blog-card">
    {% if post.thumbnail %}
    <a href="{{ post.url | relative_url }}" class="blog-card__thumbnail-link">
      <img class="blog-card__thumbnail" src="{{ post.thumbnail | relative_url }}" alt="{{ post.title }}">
    </a>
    {% endif %}
    <div class="blog-card__content">
      <h2 class="blog-card__title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <p class="blog-card__meta">
        <i class="fa fa-calendar" aria-hidden="true"></i>
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
        &nbsp;&middot;&nbsp;
        <i class="fa fa-clock-o" aria-hidden="true"></i>
        {% assign words = post.content | number_of_words %}
        {% assign minutes = words | divided_by: 160 %}
        {% if minutes < 1 %}1{% else %}{{ minutes }}{% endif %} min read
      </p>
      {% if post.tldr %}
      <p class="blog-card__tldr"><strong>TL;DR:</strong> {{ post.tldr }}</p>
      {% endif %}
      <a href="{{ post.url | relative_url }}" class="blog-card__readmore">Read more &rarr;</a>
    </div>
  </div>
{% endfor %}
{% endif %}
</div>
