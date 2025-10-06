# Personal Blog & Newsletter Site

A Jekyll-based personal website for blogging and newsletters, optimized for GitHub Pages.

## Features

- 📝 **Blog** with post categories and tags
- 📧 **Newsletter** support with archive
- 🎨 **Responsive design** that works on all devices
- 🚀 **GitHub Pages** compatible
- 📊 **SEO optimized** with meta tags and sitemap
- 🔍 **Search engine friendly** URLs
- 📱 **Social media** integration ready

## Quick Start

### 1. Setup GitHub Repository

1. Create a new repository named `username.github.io` (replace `username` with your GitHub username)
2. Clone this repository to your local machine
3. Push the code to your new repository

### 2. Configure Your Site

Edit `_config.yml` to customize your site:

```yaml
title: Your Blog Name
email: your-email@example.com
description: Your site description
url: "https://username.github.io"
author:
  name: Your Name
  email: your-email@example.com
```

### 3. Customize Content

- **About Page**: Edit `about.md` with your personal information
- **Homepage**: Modify `index.html` to match your style
- **Colors & Styling**: Update `assets/css/style.css`

### 4. Enable GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" section
3. Select "GitHub Actions" as the source
4. Your site will be available at `https://username.github.io`

## Creating Content

### Blog Posts

Create new blog posts in the `_posts` directory with the format:
```
YYYY-MM-DD-title-of-post.md
```

Example post structure:
```yaml
---
layout: post
title: "Your Post Title"
date: 2024-10-06 10:00:00 -0000
categories: [category1, category2]
tags: [tag1, tag2]
author: Your Name
excerpt: "Brief description of your post"
---

Your post content here...
```

### Newsletter Issues

Create newsletter issues in the `_newsletters` directory:

```yaml
---
layout: newsletter
title: "Newsletter Title"
date: 2024-10-06 10:00:00 -0000
issue: 1
author: Your Name
excerpt: "Brief description of this issue"
---

Your newsletter content here...
```

## Local Development

To run the site locally:

1. Install Ruby and Bundler
2. Run `bundle install` to install dependencies
3. Run `bundle exec jekyll serve` to start the development server
4. Visit `http://localhost:4000` to see your site

## Customization

### Adding Newsletter Signup

Replace the newsletter signup forms in:
- `newsletters.html`
- `_layouts/newsletter.html`

With your preferred service (Mailchimp, ConvertKit, etc.).

### Styling

- Main CSS: `assets/css/style.css`
- Colors and fonts can be customized at the top of the stylesheet
- The design is mobile-first and responsive

### Adding Features

The site supports additional Jekyll plugins. Add them to:
- `_config.yml` in the `plugins` section
- `Gemfile` in the `:jekyll_plugins` group

## Repository Structure

```
├── _layouts/           # Page templates
├── _posts/            # Blog posts
├── _newsletters/      # Newsletter issues
├── _includes/         # Reusable components
├── _sass/            # Sass stylesheets
├── assets/           # CSS, JS, images
├── .github/          # GitHub Actions workflows
├── _config.yml       # Jekyll configuration
├── Gemfile           # Ruby dependencies
├── index.html        # Homepage
├── blog.html         # Blog index
├── newsletters.html  # Newsletter index
└── about.md          # About page
```

## Support

If you encounter any issues:
1. Check the [Jekyll documentation](https://jekyllrb.com/)
2. Review [GitHub Pages documentation](https://docs.github.com/en/pages)
3. Ensure your `_config.yml` settings are correct

## License

This project is open source and available under the MIT License.