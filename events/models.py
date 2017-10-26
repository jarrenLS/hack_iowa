from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=500, unique=True)
    map_url = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.name


class Attendee(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    

class Event(models.Model):
    location = models.ForeignKey(Location)
    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    attendees = models.ManyToManyField(Attendee)
    
    def __str__(self):
        return "{title} ({location}) at {time}".format(title=self.title,
                                                       location=self.location,
                                                       time=self.time)
