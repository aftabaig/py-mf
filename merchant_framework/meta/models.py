import datetime

from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField('Branch Name', max_length=255, blank=False)
    address = models.CharField('Branch Address', max_length=1024, blank=False)
    latitude = models.FloatField('Latitude', default=0.0)
    longitude = models.FloatField('Longitude', default=0.0)
    postcode = models.CharField('Postcode', max_length=16, blank=False)
    telephone = models.CharField('Telephone #', max_length=32, blank=True)
    fax = models.CharField('Fax #', max_length=32, blank=True)
    emailAddress = models.CharField('Email Address', max_length=32, blank=False)
    weekdayTimings = models.CharField('Opening Hours (Weekdays)', max_length=16)
    saturdayTimings = models.CharField('Opening Hours (Saturdays)', max_length=16)
    createdAt = models.DateTimeField('Created At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())
    updatedAt = models.DateTimeField('Updated At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())


class Contact(models.Model):
    name = models.CharField('Contact Name', max_length=255, blank=False)
    jobRole = models.CharField('Job Role', max_length=64, blank=False)
    branch = models.ForeignKey('Branch', default=0)
    contactNumber = models.CharField('Contact #', max_length=32, blank=True)
    mobileNumber = models.CharField('Mobile #', max_length=32, blank=True)
    emailAddress = models.CharField('Email Address', max_length=64, blank=False)
    profileImageUrl = models.CharField("Profile Pic", max_length=1024, blank=True)
    createdAt = models.DateTimeField('Created At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())
    updatedAt = models.DateTimeField('Updated At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())


class Deal(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField("Description", max_length=255, blank=False)
    info = models.CharField("Deal Info", max_length=1024, blank=True)
    availability = models.DateTimeField('Available till')
    telephone = models.CharField('Telephone #', max_length=32, blank=True)
    availableOnline = models.BooleanField('Online')
    dealImageUrl = models.CharField('Deal Image', max_length=1024, blank=True)
    createdAt = models.DateTimeField('Created At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())
    updatedAt = models.DateTimeField('Updated At', auto_now=True, auto_now_add=True, default=datetime.datetime.now())


class DealBranch(models.Model):
    branch = models.ForeignKey('Branch')
    deal = models.ForeignKey('Deal')