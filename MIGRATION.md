# Minimal al-folio Website Template — Migration Summary

## What Was Created

Your website has been transformed into a **minimal, static Jekyll template** inspired by al-folio. Here's what was set up:

### Directory Structure

```
pirahansiah.github.io/
├── _layouts/                  # HTML templates (base, default, page)
├── _includes/                 # Reusable components (head, nav, footer)
├── _pages/                    # Content pages
│   ├── about.md              # About page
│   ├── projects.md           # Projects portfolio
│   └── writing.md            # Writing/blog section
├── assets/
│   └── css/
│       └── style.css         # Minimal styling (light/dark mode)
├── index.md                  # Homepage
├── feed.xml                  # Atom RSS feed
├── _config.yml               # Jekyll configuration
├── Gemfile                   # Ruby dependencies (minimal)
├── run.sh                    # Build & serve script
└── README.md                 # Documentation
```

### Key Features

✅ **Minimal Dependencies**
- Only Jekyll + jekyll-feed
- No heavy themes or frameworks
- No Docker, build tools, or test packages

✅ **Static Content**
- Pure Markdown files for all content
- No JavaScript required (optional)
- Clean semantic HTML

✅ **al-folio Inspired Design**
- Clean, modern CSS styling
- Light/dark mode support
- Responsive mobile design
- Minimal color palette

✅ **Easy Navigation**
- Simple navbar with links to main sections
- Organized page structure
- Automatic feed generation

### Updated Files

| File | Changes |
|------|---------|
| `_config.yml` | Minimal Jekyll config, null theme, feed plugin |
| `Gemfile` | Only jekyll, jekyll-feed, rouge, webrick |
| `index.md` | Converted to markdown layout (from HTML) |
| `run.sh` | Simplified build & serve script |
| `README.md` | Complete setup and usage documentation |

### New Files Created

**Layouts** (`_layouts/`):
- `base.html` — Root template with nav/footer
- `default.html` — Extends base with article wrapper
- `page.html` — Extends default with page header

**Includes** (`_includes/`):
- `head.html` — Metadata, styles, favicon
- `nav.html` — Navigation bar with links
- `footer.html` — Footer with social links

**Pages** (`_pages/`):
- `about.md` — Bio, skills, contact
- `projects.md` — Project portfolio and links
- `writing.md` — Article/blog index

**Styling** (`assets/css/`):
- `style.css` — Complete minimal design system

**Other**:
- `feed.xml` — Atom feed template

## How to Use

### Local Development

```bash
# Navigate to repo
cd /Volumes/4tb/2026-6/pirahansiah.github.io

# Install dependencies
bundle install

# Start dev server
./run.sh
# Or manually:
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Deployment

The site is ready for GitHub Pages:
```bash
git add .
git commit -m "Migrate to minimal al-folio template"
git push origin main
```

Your site will be live at `https://pirahansiah.github.io`

## Customization

### Update Site Info
Edit `_config.yml`:
```yaml
title: Your Name
author: Your Name
email: your@email.com
url: https://yoursite.com
description: Your tagline
```

### Edit Navigation
Edit `_includes/nav.html` to add/remove menu links.

### Change Colors
Edit `_config.yml` or `assets/css/style.css` CSS variables:
```css
:root {
  --primary-color: #4a5568;     /* Links, accents */
  --text-color: #1a202c;        /* Main text */
  --light-text: #718096;        /* Secondary text */
  --border-color: #e2e8f0;      /* Dividers */
  --code-bg: #f7fafc;           /* Code block background */
}
```

### Add Content
1. **New page**: Create `_pages/your-page.md` with YAML frontmatter
2. **Update sections**: Edit content in existing `_pages/*.md` files
3. **Update homepage**: Edit `index.md`

## Design Principles

- **Static-first**: No build complexity, pure Markdown
- **Minimal**: Only essentials — no bloat
- **Semantic HTML**: Clean, accessible markup
- **Dark mode**: Automatic respects system preference
- **Mobile-friendly**: Responsive design included
- **Fast**: No JavaScript required, instant builds

## Next Steps

1. ✅ Test locally: `./run.sh`
2. ✅ Customize site info in `_config.yml`
3. ✅ Update content pages as needed
4. ✅ Push to GitHub Pages
5. ✅ (Optional) Link to PKM repo in about/projects pages

## Notes

- The old `assets/js/app.js` and complex HTML have been removed
- `site.md` from PKM repo can still be linked/referenced in content
- No breaking changes to GitHub Pages deployment
- All content is backward compatible with standard Jekyll

---

**Done!** Your minimal Jekyll website is ready to go. No frameworks, no Docker, no build complexity — just clean markdown and static HTML.
