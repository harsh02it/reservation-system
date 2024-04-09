from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Table, Reservation
from .forms import ReservationForm

def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('manage_reservation', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})

def manage_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('manage_reservation', reservation_id=reservation.id)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'manage_reservation.html', {'form': form})

def assign_table(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table.status = 'Reserved'
            reservation.table.save()
            reservation.save()
            return redirect('assign_table', reservation_id=reservation.id)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'assign_table.html', {'form': form})