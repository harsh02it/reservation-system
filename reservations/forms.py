from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'reservation_time', 'number_of_people', 'status']