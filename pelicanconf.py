#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'if1live'
SITENAME = u'Static Blog Sample'
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
SOCIAL = (('Twitter', 'https://twitter.com/if1live'),
          ('GitHub-Repo', 'https://github.com/static-blog-sample/'),
          ('GitHub-Writer', 'https://github.com/if1live'))

DEFAULT_PAGINATION = 10
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

STATIC_PATHS = ['static']