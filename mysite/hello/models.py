from django.db import models
from django import forms


class Names(models.Model):
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
