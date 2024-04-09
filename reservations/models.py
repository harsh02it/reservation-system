from django.db import models

class Reservation(models.Model):
    customer = models.CharField(max_length=100)
    table = models.IntegerField()
    reservation_time = models.DateTimeField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=10)