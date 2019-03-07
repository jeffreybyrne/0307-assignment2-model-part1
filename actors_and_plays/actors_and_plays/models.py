from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Play(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
