from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
