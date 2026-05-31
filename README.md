# Farshid Pirahansiah's Website

A minimal, static Jekyll-based personal website inspired by [al-folio](https://github.com/alshedivat/al-folio).

## Quick Start

### Build Locally

```bash
# Install dependencies (once)
bundle install

# Build and serve
bundle exec jekyll serve
```

Visit `http://localhost:4000` in your browser.

## Structure

```
.
├── _layouts/          # HTML templates
├── _includes/         # Reusable HTML components
├── _pages/            # Content pages (about, projects, writing)
├── assets/css/        # Styling
├── index.md           # Homepage
├── _config.yml        # Jekyll configuration
├── Gemfile            # Ruby dependencies
└── README.md          # This file
```

## Pages

- **Home** (`index.md`) - Introduction and featured work
- **About** (`_pages/about.md`) - Bio and skills
- **Projects** (`_pages/projects.md`) - Project portfolio
- **Writing** (`_pages/writing.md`) - Blog/articles

## Customization

### Update Site Info

Edit `_config.yml`:
```yaml
title: Your Name
author: Your Name
url: https://yoursite.com
```

### Navigation

Edit `_includes/nav.html` to change menu links.

### Styling

Edit `assets/css/style.css` for colors, fonts, and layout.

## Deploy

This site is designed to deploy directly with GitHub Pages. Just push to the `main` branch of your `username.github.io` repository.

## Related

- **Content Repository**: [PKM](https://github.com/pirahansiah/PKM.git) - Main knowledge base
- **Template Inspiration**: [al-folio](https://github.com/alshedivat/al-folio)

## License

MIT License - See [LICENSE](LICENSE) file.

---

Built with Jekyll. No frameworks, no build tools, just markdown and HTML.