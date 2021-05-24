from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
