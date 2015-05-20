#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEFAULT_DATE = 'fs'
AUTHOR = u'Marek'
SITENAME = u'Úlohy pro výuku programování'
SITEURL = 'http://spseol.github.io/ulprog'

PATH = 'content'

THEME = 'theme-myResponsivePelican'
TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 200


TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Py.cz', 'http://py.cz'),
         ('Python.cz', 'http://python.cz/'),
         ('Python.org', 'http://python.org/'),
         ('Python documentation', 'https://docs.python.org/'),
         ('Česká encyklopedie algoritmů',
          'http://www.itnetwork.cz/uzitecne-algoritmy-pro-programovani'),
         ('Stack Overflow', 'http://stackoverflow.com/'),
         ('Úvod do Tkinter ', 'http://tkinter.programujte.com'),
         ('Tkinter reference',
          'http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html'),
         ('Korespondenční seminář z programování', 'https://ksp.mff.cuni.cz/'),
         ('CzechFlaskDoc', 'http://spseol.github.io/CzechFlaskDoc/'),
         ('PyQt4Doc', 'http://spseol.github.io/PyQt4Doc/'),
         ('PyGame -- české tutoriály', 'http://www.geon.wz.cz/pygame/'),
         ('Jak se naučit programovat', 'http://jaksenaucitprogramovat.py.cz/'),
         ('Učíme se programovat v jazyce Python 3', 'http://howto.py.cz/'),
         ('Sallyx/Python', 'http://www.sallyx.org/sally/python/'),
         ('Ponořme se do Pythonu 3',
          'http://diveintopython3.py.cz/index.html'),
         ('Létající cirkus', 'http://www.root.cz/serialy/letajici-cirkus/'),
         ('MatPlotLib', 'http://hroch/~nozka/python/matplotlib/'),
         # ('', ''),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/spseol/'),
          ('spseol.github.io', 'http://spseol.github.io/'),
          ('Facebook', 'https://cs-cz.facebook.com/spseol'),
          ('G+', 'https://plus.google.com/118347382558771670752'),
          ('SPŠE Olomouc', 'http://www.spseol.cz/'),
          ('~Nožka', 'http://hroch.spseol.cz/~nozka/'),
          ('Pelican', 'http://getpelican.com/'),
          )

DEFAULT_PAGINATION = False
DEFAULT_PAGINATION = 20

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

DOCUTILS_SETTINGS = {'smart_quotes': 'yes',
                     'initial_header_level': 3,
                     }

EXTRA_PATH_METADATA = {'extra/README': {'path': 'README.md'},
                       'extra/.nojekyll': {'path': '.nojekyll'},
                       }

PIWIK_URL = 'yanek.cz/piwik'
PIWIK_SITE_ID = 6
