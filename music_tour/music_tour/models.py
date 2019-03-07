from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    instrument = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name


class Setlist(models.Model):
    name = models.CharField(max_length=255)
    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    setlist = models.ManyToManyField(Setlist)

    def __str__(self):
        return self.name
