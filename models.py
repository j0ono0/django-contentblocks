from datetime import datetime
from django.db import models
from django.utils import timezone


class ContentBlock(models.Model):
     
    class Meta:
        ordering = ['location', 'weight', 'start_datetime', 'end_datetime']

    LOCATIONS = [
        ('home','Home'),
        ('footer','Footer'),
    ]

    DISPLAY_GROUPS = [
        ('all', 'All users'),
        ('anonymous', 'Anonymous users'),
        ('authenticated', 'Authenticated users'),
    ]
    location = models.CharField(max_length=100, choices=LOCATIONS, blank=False)
    content = models.TextField(blank=False, default='')
    weight =  models.SmallIntegerField(default=0)
    display_group = models.CharField(max_length=50,choices=DISPLAY_GROUPS, default='all', blank=False)
    start_datetime = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_datetime = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f'{self.get_location_display()} : {self.weight} : {self.content[:50]}'
