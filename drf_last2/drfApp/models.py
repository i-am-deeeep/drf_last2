from django.db import models

# Create your models here.
class Platform(models.Model):
    name=models.CharField(max_length=30)
    free=models.BooleanField()
    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=900)
    ott=models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='movies')
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
