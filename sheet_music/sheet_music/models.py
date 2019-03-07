from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateField()

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sheet(models.Model):
    name = models.CharField(max_length=255)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
