#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import conf


for app in conf.settings.INSTALLED_APPS:
    try:
        print("import", __import__("%s.freeadmin" % app))
    except ImportError as e:
        print("app has no module freeadmin")