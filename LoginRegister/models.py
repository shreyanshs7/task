# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)