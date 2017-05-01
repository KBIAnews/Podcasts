# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bakery.views import BuildableListView, BuildableDetailView

from .models import Show

# Create your views here.

class ShowListView(BuildableListView):
    queryset = Show.objects.all()
    model = Show

class ShowDetailView(BuildableDetailView):
    model = Show
    template_name = 'shows/show_detail.html'