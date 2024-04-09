from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)

class Table(models.Model):
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=200)