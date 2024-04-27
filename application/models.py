from distutils.command.upload import upload
from email.policy import default
from random import choices
from statistics import mode
from turtle import color
from unicodedata import decimal
from django.db import models
from datetime import datetime

class drugs(models.Model):
 name = models.CharField(max_length = 50 , default= '' , verbose_name= "Name")
 description=models.TextField(max_length = 255)
 price = models.DecimalField(max_digits= 7 ,decimal_places = 3)
 category = models.TextField(max_length = 255,default='')
 hour = models.TimeField(null=True , blank = True)
 datetime= models.DateTimeField(default= datetime.now)
 image = models.ImageField(upload_to = 'photos/%y/%m/%d',default= '')

 def __str__(self):
        return str(self.name)
 class Meta:
        verbose_name = 'My-drugs'
        ordering = ['-price']
