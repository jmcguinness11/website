#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'John McGuinness'
SITENAME = u"John McGuinness"
SITEURL = ''

PATH = 'content'
THEME = './pure-single'
TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#images
COVER_IMG_URL = SITEURL + '/images/ND_Stadium.jpg'
PROFILE_IMG_URL = SITEURL + '/images/linkedin_photo.jpg'
FAVICON_URL = SITEURL + '/images/mcguinness_large.gif'
#FAVICON_URL = SITEURL + '/images/jfavicon.png'


# Social widget
SOCIAL = (('github', 'http://github.com/jmcguinness11'),
          ('linkedin', 'https://www.linkedin.com/in/john-mcguinness-486a34126/'),)

#DEFAULT_PAGINATION = False

SIDEBAR_DIGEST = 'University of Notre Dame Class of 2019'
MENUITEMS = (('About me', SITEURL + '/pages/about-me.html'), 
            ('Posts', SITEURL + '/'))

STATIC_PATHS = ['images']


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
