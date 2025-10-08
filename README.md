# Personal Blog & Newsletter Site

A clean, single-column Jekyll website using the Minimal Mistakes theme with dirt skin. Built for GitHub Pages.

## Features

- 📝 **Clean single-column layout** - no sidebar clutter
- 📧 **Newsletter** support with archive
- 🎨 **Minimal Mistakes theme** with professional dirt skin
- 🚀 **GitHub Pages** compatible
- 📊 **SEO optimized** with meta tags and sitemap
- 📱 **Fully responsive** design

## Site Structure

- **Homepage**: Clean introduction and recent thoughts
- **Blog**: All your technical posts
- **Newsletter**: Archive of newsletter issues
- **About**: Your full profile and contact information (author details only appear here)

## Creating Content

### Blog Posts

Create new posts in the `_posts` directory using this naming format:
```
YYYY-MM-DD-your-post-title.md
```

**Example:** `_posts/2024-10-08-my-new-post.md`

```yaml
---
layout: single
title: "Your Post Title"
date: 2024-10-08 10:00:00 -0000
categories: [ai, engineering]
tags: [machine-learning, aws, python]
author: Your Name
excerpt: "Brief description that appears in post previews"
---

# Your Post Title

Write your post content here using Markdown.

## Subheading

- Bullet points work
- **Bold text** and *italic text*
- `code snippets`

```python
# Code blocks with syntax highlighting
def hello_world():
    print("Hello, World!")
```
```

### Newsletter Issues

Create newsletters in the `_newsletters` directory:

**Example:** `_newsletters/2024-10-08-newsletter-title.md`

```yaml
---
layout: single
title: "Newsletter Title - Issue #2"
date: 2024-10-08 10:00:00 -0000
issue: 2
author: Your Name
excerpt: "Brief description of this newsletter issue"
---

# Newsletter Title - Issue #2

Your newsletter content here...

## This Week's Highlights

- Item 1
- Item 2

## Links Worth Sharing

- [Link Title](https://example.com)
```

## Local Development

To run the site locally:

1. Install Ruby and Bundler
2. Run `bundle install` to install dependencies
3. Run `bundle exec jekyll serve` to start the development server
4. Visit `http://localhost:4000` to see your site

## Quick Publishing Workflow

1. **Write a new post**: Create file in `_posts/` with proper naming and frontmatter
2. **Preview locally**: Run `bundle exec jekyll serve` to test
3. **Commit and push**: Git will automatically deploy to GitHub Pages
4. **View live site**: Changes appear at your GitHub Pages URL in ~1 minute

## Repository Structure

```
├── _posts/            # Your blog posts (YYYY-MM-DD-title.md)
├── _newsletters/      # Newsletter issues
├── _data/            # Navigation configuration
├── assets/css/       # Styling (minimal-mistakes theme + dirt skin)
├── _config.yml       # Site configuration
├── index.md          # Homepage
├── blog.md           # Blog listing page
├── newsletters.md    # Newsletter archive
└── about.md          # About page (only page with author profile)
```

## Configuration

Main settings are in `_config.yml`:
- Site title, description, and URL
- Author information (shows only on About page)
- Theme: `minimal_mistakes_skin: "dirt"`
- Social media links

## Tips

- **Markdown support**: Full Markdown syntax with syntax highlighting
- **SEO friendly**: Automatic meta tags and sitemap generation
- **Mobile first**: Responsive design works on all devices
- **Fast loading**: Minimal theme optimized for speed