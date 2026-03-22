---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---

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

<!-- ============================================================
     Visitor map — shows where the current reader is visiting from.
     Uses Leaflet.js + ipapi.co (free, ~1000 req/day).
     No account or backend required.
     ============================================================ -->
<div class="visitor-map-section">
  <h3 class="visitor-map-title">
    <i class="fa fa-globe" aria-hidden="true"></i> Readers Around the World
  </h3>
  <div id="visitor-map"></div>
  <p class="visitor-map-note">
    Your approximate location is shown based on your IP address.
    Location data is not stored. Powered by
    <a href="https://leafletjs.com" target="_blank" rel="noopener">Leaflet</a>
    &amp; <a href="https://ipapi.co" target="_blank" rel="noopener">ipapi.co</a>.
  </p>
</div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV/XN/WPeM=" crossorigin=""></script>
<script>
(function () {
  var map = L.map('visitor-map', {
    center: [20, 10],
    zoom: 1,
    zoomControl: true,
    scrollWheelZoom: false
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 12,
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  /* Custom marker: pulsing dot */
  var pulsingIcon = L.divIcon({
    className: '',
    html: '<div style="width:16px;height:16px;border-radius:50%;background:#0077cc;border:3px solid #fff;box-shadow:0 0 0 2px #0077cc, 0 0 12px rgba(0,119,204,0.6);"></div>',
    iconSize: [16, 16],
    iconAnchor: [8, 8],
    popupAnchor: [0, -12]
  });

  fetch('https://ipapi.co/json/')
    .then(function (r) { return r.json(); })
    .then(function (d) {
      if (!d.latitude || !d.longitude) return;
      var lat = d.latitude, lng = d.longitude;
      var label = [d.city, d.region, d.country_name].filter(Boolean).join(', ');

      L.marker([lat, lng], { icon: pulsingIcon })
        .addTo(map)
        .bindPopup(
          '<strong>You\'re visiting from</strong><br>' + label,
          { closeButton: false }
        )
        .openPopup();

      map.setView([lat, lng], 4, { animate: true });
    })
    .catch(function () {
      /* geolocation failed — world map is still useful */
    });
})();
</script>
