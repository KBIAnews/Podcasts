# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Show (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="shows/images")
    feed_url = models.URLField(
        "Podcast (RSS) Feed URL",
        max_length=1024,
        null=True,
        blank=True)
    itunes_url = models.URLField(
        "Apple Podcasts/iTunes Page URL",
        max_length=1024,
        null=True,
        blank=True)
    stitcher_url = models.URLField(
        "Stitcher Page URL",
        max_length=1024,
        null=True,
        blank=True)
    google_url = models.URLField(
        "Google Play Podcasts Page URL",
        max_length=1024,
        null=True,
        blank=True)

    class Meta:
        ordering = ['slug']

    def get_absolute_url(self):
        return "/shows/%s/" % self.slug

    def __str__(self):
        return "%s" % self.name