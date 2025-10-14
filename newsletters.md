---
layout: archive
title: "Newsletter"
permalink: /newsletters/
---
My intention for this newsletter is to serve as an quick summary of the developments in AI. 

While there might a ton of newsletters focusing on AI, but, I didn't find a good one which summarizes all the developments everyday. Furthermore, I created this for my own sanity, there are way too many developments, blogs, and research articles in this area. But, I often find my self not develling into any topic due to the sheer stress to not knowing where to start. 

This newsletter focuses on providing a brief summary of the trending topics everyday to keep me upto date. 

I'm not the one personally curating all the developments instead I created an agent which uses OpenAI, Anthropic, ArXiv, and other popular websites to find relevant data.

Any suggestion is welcome!

{% for newsletter in site.newsletters reversed %}
  <div class="archive__item">
    <h2 class="archive__item-title"><a href="{{ newsletter.url | relative_url }}">{{ newsletter.title }}</a></h2>
    <p class="page__date">{{ newsletter.date | date: "%B %d, %Y" }}{% if newsletter.issue %} • Issue #{{ newsletter.issue }}{% endif %}</p>
    <p class="archive__item-excerpt">{{ newsletter.excerpt | strip_html | truncatewords: 30 }}</p>
  </div>
{% endfor %}