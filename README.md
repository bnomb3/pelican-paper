# Pelican Paper Theme

A minimalist, clean, and typography-focused theme for [Pelican](https://getpelican.com/), built with Tailwind CSS.

## Features

*   **Clean Typography**: Optimized for reading with a serif/sans-serif pairing.
*   **Dark Mode**: Automatic detection + manual toggle.
*   **Responsive**: Mobile-friendly design.
*   **Features**:
    *   Archives, Categories, Tags, and Authors pages.
    *   Pagination.
    *   Syntax highlighting (Pygments).
*   **Bilingual posts**: A language switcher (e.g. `EN / ZH`) on translated posts and in post listings.

## Installation

1.  Add this repository to your site's `themes` directory. As a git submodule (recommended, pins a theme version):
    ```bash
    git submodule add https://github.com/bnomb3/pelican-paper themes/paper
    ```
    or as a plain clone:
    ```bash
    git clone https://github.com/bnomb3/pelican-paper themes/paper
    ```

2.  Set the theme in your `pelicanconf.py`:
    ```python
    THEME = 'themes/paper'
    ```

## Settings

All optional. These are standard Pelican settings unless marked *(theme)*.

| Setting | Effect |
|---|---|
| `SITESUBTITLE` | Line shown under the site name. HTML is allowed. Give a list to show one at random on each page load, e.g. `['Hello', 'Bonjour']` (the first is the no-JavaScript fallback). |
| `MENUITEMS` | Extra header links, e.g. `(('GitHub', 'https://github.com/you'),)`. |
| `DISPLAY_PAGES_ON_MENU` | Show your pages (About, …) in the header. Default `True`. |
| `FOOTER_TEXT` *(theme)* | Replaces the default footer (`© <year> <AUTHOR> · Powered by Pelican and Paper`). HTML is allowed. |

## Translations

The theme uses Pelican's built-in translations. Give the translated file the **same `Slug`** and its own `Lang`:

```markdown
Title: 设计哲学：少即是多
Slug: design-philosophy
Lang: zh
```

Pelican links the two and the theme shows a language switcher on both posts and wherever the post is listed.
Listings show the version in `DEFAULT_LANG`. To list a different version instead, add `Translation: true`
to the one you *don't* want listed.

## Development

The `demo/` folder is a Pelican site with sample content (placeholder posts, code blocks, a translated post)
that uses this theme (`THEME = '..'`). Preview your changes with [uv](https://docs.astral.sh/uv/):

```bash
cd demo
uv sync
uv run make devserver    # http://localhost:8000
```

### CSS

This theme uses Tailwind CSS v4 (pinned in `package.json`). `static/css/input.css` is the source; it scans
`templates/` for class names. The compiled `static/css/output.css` is committed so the theme works without a
build step or Node: **rebuild it after adding new classes to the templates.**

```bash
npm install        # installs the pinned Tailwind version
npm run watch      # rebuild on every template/CSS change (run alongside the demo devserver)
npm run build      # one-off rebuild
```

To upgrade Tailwind, change both versions in `package.json`, run `npm install && npm run build`, and check the
demo site.

## License

MIT
