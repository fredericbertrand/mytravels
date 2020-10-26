from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.name