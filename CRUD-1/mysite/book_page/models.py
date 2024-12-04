from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
