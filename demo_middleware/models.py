from django.db import models

# Create your models here.

class Newstats(models.Model):
    win = models.IntegerField()
    mac = models.IntegerField()
    iph = models.IntegerField()
    android = models.IntegerField()
    oth = models.IntegerField()