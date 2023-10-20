from django.db import models

# Create your models here.
class Groups(models.Model):
    title = models.CharField()
    slug =models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title