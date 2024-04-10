from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.http import HttpResponse
from reservations.models import Reservation
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from .models import Reservation

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
    db_status = "View reservations"
    reservations = Reservation.objects.all().order_by('-reservation_time')  # Fetch from Django

    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ismaster')
        db_status = "MongoDB connection successful"

        # Fetch reservations from MongoDB (assuming a collection named 'reservations')
        mongo_reservations = list(client['pysquad-reservation-system']['Reservation'].find({}))
        print("Data is ", list(mongo_reservations))

        # (Optional) Process or combine data from MongoDB if needed
    except ConnectionFailure:
        db_status = "MongoDB connection failed"
        mongo_reservations = []

    return render(request, 'reservations/view_reservations.html', {
        'reservations': reservations,
        'db_status': db_status,
        'mongo_reservations': mongo_reservations,  # Include data from MongoDB
    })