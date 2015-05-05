#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marek'
SITENAME = u'\xdalohy pro v\xfduku programov\xe1n\xed'
SITEURL = 'http://spseol.github.io/ulprog/'

PATH = 'content'

THEME = 'ResponsivePelican'
TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 200


TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('SPŠE Olomouc', 'http://www.spseol.cz/'),
         ('spseol.github.io', 'http://spseol.github.io/'),
         ('~Nožka', 'http://hroch.spseol.cz/~nozka/'),
         ('Python.org', 'http://python.org/'),
         ('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/spseol/'),
          ('Facebook', 'https://cs-cz.facebook.com/spseol'),
          ('G+', 'https://plus.google.com/118347382558771670752'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'extra',
    'headerid(level=2)',
    'toc',
    'linksShortcuts:Shortcuts',
]

STATIC_PATHS = ['extra', ]
EXTRA_PATH_METADATA = {'extra/README': {'path': 'README.md'},
                       'extra/.nojekyll': {'path': '.nojekyll'},
                       }
