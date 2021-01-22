from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=200)
    description=models.TextField()
    price=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    year=models.CharField(max_length=10)
    date=models.CharField(max_length=10)

