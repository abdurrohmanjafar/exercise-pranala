from django.db import models

# Create your models here.


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    review = models.TextField(max_length=100)
    rating = models.IntegerField()
