# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Show, Episode

# Register your models here.

admin.site.register(Show)
admin.site.register(Episode)