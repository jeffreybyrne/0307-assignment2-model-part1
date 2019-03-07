from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Issue(models.Model):
    name = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
