#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'if1live'
SITENAME = u'Demo'
SITEURL = ''

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = u'ko'

DEFAULT_DATE_FORMAT = '%Y/%m/%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('libsora.so', 'http://libsora.so/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/if1live'),)

DEFAULT_PAGINATION = 10
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['static']


PLUGIN_PATH = 'ext/pelican-plugins'
THEME = 'ext/pelican-sora'

PLUGINS = [
    'assets',
	'tipue_search',
	'sitemap',
]

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITE_DESCRIPTION = u'static blog generator sample'
SITESUBTITLE = ''
SITE_LICENSE = ''
RECENT_ARTICLES_COUNT = 10

DNSEVER_BANNER = True