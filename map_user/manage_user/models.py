# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mst_users(models.Model):
       usr_id=models.AutoField(primary_key=True)
       usr_name=models.CharField(max_length=50,null=False,blank=False)
       usr_email=models.CharField(max_length=50,null=False,blank=False)
       usr_password=models.CharField(max_length=50,null=False,blank=False)
       usr_deleted=models.CharField(max_length=1,null=False,blank=False)
       usr_enabled=models.CharField(max_length=1,null=False,blank=False)
       usr_created_datetime=models.DateTimeField(auto_now_add=True)
       usr_location=models.CharField(max_length=50,null=False,blank=False)


class mst_users_form(ModelForm)
       usr_name=forms.CharField(max_length=50,null=False,blank=False)
       usr_email=forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'text'}),required=True)
       usr_password=forms.CharField(label='Other',widget=forms.TextInput(attrs={'class':'text'\
                                                                         }),required=True)
       
       class Meta:
              model=mst_users
              exclude=('usr_location','usr_enabled','usr_deleted','usr_created_datetime')
