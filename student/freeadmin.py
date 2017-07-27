#!/usr/bin/env python
# -*- coding: utf-8 -*-

from student import models
from freeadmin.base_admin import site

site.register(models.TestTable)

