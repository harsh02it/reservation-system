from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

def make_reservation(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'reservations/make_reservation.html', {'form': form})

def manage_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
    return render(request, 'reservations/manage_reservation.html', {'form': form})

def assign_table(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
    return render(request, 'reservations/assign_table.html', {'form': form})

def view_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/view_reservations.html', {'reservations': reservations})