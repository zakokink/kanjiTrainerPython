from datetime import datetime
from django.db import models
from django.db.models import ForeignKey


class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Kanji(models.Model):
    kanji = models.CharField(max_length=200)
    idNummer = models.IntegerField(null=True, blank=True)
    bedeutungen = models.CharField(max_length=500, null=True, blank=True)
    sinoLesungen = models.CharField(max_length=200, null=True, blank=True)
    japLesungen = models.CharField(max_length=500, null=True, blank=True)
    woerter =  models.CharField(max_length=500, null=True, blank=True)
    failedCount = models.IntegerField(null=True, blank=True, default=0)
    lastPositive = models.DateField(default=datetime.now)
    language = ForeignKey(Language, on_delete=models.PROTECT, default=0)
    user = ForeignKey(User, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return str(self.kanji) + ' - ' + str(self.bedeutungen)
