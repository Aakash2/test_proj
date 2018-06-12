# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mst_users(models.Model):
       usr_id=models.AutoField(primary_key=True)
       usr_name=models.CharField(max_length=50,null=False,blank=False)
