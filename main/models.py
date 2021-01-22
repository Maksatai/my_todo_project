from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    price=models.IntegerField
    genre=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    year=models.IntegerField
    date=models.DateField(auto_now_add=False)

