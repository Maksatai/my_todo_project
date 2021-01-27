from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=200)
    description=models.TextField()
    price=models.CharField(max_length=50)
    genre=models.TextField()
    author=models.CharField(max_length=100)
    year=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_closed=models.BooleanField(default=False)
    is_favorite=models.BooleanField(default=False)
