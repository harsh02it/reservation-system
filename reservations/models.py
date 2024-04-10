from django.db import models
from djongo import models as djongo_models


class Reservation(models.Model):
    def __str__(self):
        return f'Reservation {self._id}'

    _id = djongo_models.ObjectIdField()
    customer = models.CharField(max_length=200)
    table = models.IntegerField()
    reservation_time = models.DateTimeField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=200)

    class Meta:
        db_table = 'Reservation'