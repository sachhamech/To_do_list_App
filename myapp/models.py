from django.db import models
# Create your models here.

class To_do(models.Model):
    Task=models.CharField(max_length=200)
    Status=models.CharField(max_length=200,default='incomplete')
    def __str__(self):
        return self.Task


