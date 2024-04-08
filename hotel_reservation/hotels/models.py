from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotelName = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.hotelName