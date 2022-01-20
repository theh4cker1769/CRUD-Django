from email.mime import image
from fileinput import filename
from unicodedata import name
from django.db import models
import datetime
import os
# Create your models here.


def filename(request, filename):
    old_filename = filename
    timedate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = timedate + "_" + old_filename
    return os.path.join('uploads/', filename)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    profileImg = models.ImageField(upload_to=filename, null=True, blank=True)


class Item(models.Model):
    testName = models.CharField(max_length=100)
    testImage = models.ImageField(upload_to='uploads/', null=True, blank=True)
