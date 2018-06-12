# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mst_users(models.Model):
       usr_id=models.AutoField(primary_key=True)
       usr_name=models.CharField(max_length=50,null=False,blank=False)
       usr_email=models.CharField(max_length=50,null=False,blank=False)
       usr_deleted=models.CharField(max_length=1,null=False,blank=False)
       usr_enabled=models.CharField(max_length=1,null=False,blank=False)
       usr_created_datetime=models.DateTimeField(auto_now_add=True)
       usr_location=models.CharField(max_length=50,null=False,blank=False)


