---
layout: archive
title: "Newsletter"
permalink: /newsletters/
---

The AI Engineering Weekly - insights from building scalable AI systems at AWS, trends in LLM fine-tuning, and curated resources for ML engineers.

{% for newsletter in site.newsletters reversed %}
  <div class="archive__item">
    <h2 class="archive__item-title"><a href="{{ newsletter.url | relative_url }}">{{ newsletter.title }}</a></h2>
    <p class="page__date">{{ newsletter.date | date: "%B %d, %Y" }}{% if newsletter.issue %} • Issue #{{ newsletter.issue }}{% endif %}</p>
    <p class="archive__item-excerpt">{{ newsletter.excerpt | strip_html | truncatewords: 30 }}</p>
  </div>
{% endfor %}