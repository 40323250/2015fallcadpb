#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os

AUTHOR = '40323255'
SITENAME = '2015FALL 40323255 電腦輔助設計實習 作業'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('2015課程網頁', 'http://wordpress-2015course.rhcloud.com/'),('班級github', 'https://github.com/2015fallhw/2015fallcadpb/wiki'),('班級組別倉儲', 'http://2015fallhw.github.io/2015fallcadpb/category/g2.html'),
         ('個人github倉儲', 'https://github.com/40323255/40323255cadp/tree/gh-pages'),
         ('Python', 'http://python.org/'),('40323255 個人網頁', 'http://40323255.github.io/40323255cadp/'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('github', 'http://github.com/ametaireau'),)
          
DEFAULT_PAGINATION = 10

SITEURL = 'http://coursemdetw.github.io/reveal'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
DISQUS_SITENAME = "2015fall"
#GOOGLE_ANALYTICS = ""

# 必須絕對目錄或相對於設定檔案所在目錄
PLUGIN_PATHS = ['./../../../plugin']
PLUGINS = ['liquid_tags.notebook']
# 目錄設定相對於 reveal 下的 content 目錄
NOTEBOOK_DIR = 'notebook'


