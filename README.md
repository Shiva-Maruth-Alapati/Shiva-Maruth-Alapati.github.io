# Personal Profile Site

A clean single-page Jekyll site using the Minimal Mistakes theme. The homepage doubles as the About page so all of the content lives in `index.md`.

## Features

- 🧑‍💻 **Author-focused landing page** with profile panel enabled on the homepage
- 🎨 **Minimal Mistakes + dirt skin** out of the box
- 🚀 **GitHub Pages** ready with sitemap, SEO tags, and feed
- 📱 **Responsive layout** that works well on phones and desktops

## Customizing Content

- Update the copy in `index.md` to change the homepage/About sections.
- Adjust author information, links, and theme settings in `_config.yml`.
- Update navigation labels in `_data/navigation.yml` if you add new sections later.

## Local Development

To run the site locally:

1. Install Ruby and Bundler
2. Run `bundle install` to install dependencies
3. Run `bundle exec jekyll serve` to start the development server
4. Visit `http://localhost:4000` to see your site

## Quick Publishing Workflow

1. **Edit content**: Update markdown or configuration files.
2. **Preview locally**: Run `bundle exec jekyll serve` to test.
3. **Commit and push**: GitHub Pages rebuilds automatically.
4. **View live site**: Changes appear at your GitHub Pages URL in ~1 minute.

## Repository Structure

```
├── _data/            # Navigation configuration
├── assets/css/       # Styling (theme overrides)
├── _config.yml       # Site configuration + author info
└── index.md          # Homepage (About content)
```

## Configuration

Main settings are in `_config.yml`:
- Site title, description, and URL
- Author information (shows in the sidebar panel)
- Theme: `minimal_mistakes_skin: "dirt"`
- Social media links

## Tips

- **Markdown support**: Full Markdown syntax with syntax highlighting
- **SEO friendly**: Automatic meta tags and sitemap generation
- **Mobile first**: Responsive design works on all devices
- **Fast loading**: Minimal theme optimized for speed
