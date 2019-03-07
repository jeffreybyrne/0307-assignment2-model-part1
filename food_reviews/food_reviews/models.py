from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Critic(models.Model):
    name = models.CharField(max_length=255)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    review = models.TextField()
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.critic)
