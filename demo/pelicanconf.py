AUTHOR = 'Demo Author'
SITENAME = 'Paper Theme Demo'
SITEURL = ""

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = '..'  # the theme lives at the repo root

# Autoreload watches THEME recursively, and '..' contains this demo's own output/.
# Ignore it, or each build's writes trigger another build (an endless loop on macOS).
import os
IGNORE_FILES = ['.#*', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output', '*')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}
