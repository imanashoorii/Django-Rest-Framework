from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    creator = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
