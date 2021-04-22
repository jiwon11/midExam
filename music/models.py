from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Music(models.Model):
    music_name = models.CharField(max_length = 50)
    music_brand = models.CharField(max_length = 50)
    music_buy = models.DateTimeField(default=timezone.now)
    music_price =  models.IntegerField(default = 0)
    music_producer = models.CharField(max_length = 50)
    music_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.music_name

    def was_published_recently(self):
        return self.music_buy >= timezone.now() - datetime.timedelta(days=1)
