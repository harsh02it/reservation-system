from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.http import HttpResponse
from reservations.models import Reservation
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponse("Welcome to the home page!")

def make_reservation(request):
    if request.method == 'POST':
        # Create a new reservation
        new_reservation = Reservation(
            customer=request.POST['customer'],
            table=request.POST['table'],
            reservation_time=request.POST['reservation_time'],
            number_of_people=request.POST['number_of_people'],
            status=request.POST['status'],
        )
        new_reservation.save()

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['pysquad-reservation-system']

        # Create a dictionary that represents the new reservation
        reservation_dict = {
            'customer': new_reservation.customer,
            'table': new_reservation.table,
            'reservation_time': new_reservation.reservation_time,
            'number_of_people': new_reservation.number_of_people,
            'status': new_reservation.status,
        }

        # Insert the new reservation into MongoDB
        db['Reservation'].insert_one(reservation_dict)

        # Redirect to the view page
        return HttpResponseRedirect('/view/')

    # Render the reservation form
    return render(request, 'reservations/make_reservation.html')


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
    reservations = Reservation.objects.all().order_by('-reservation_time')

    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ismaster')
        db_status = "MongoDB connection successful"

        # Fetch reservations from MongoDB (assuming a collection named 'reservations')
        mongo_reservations = list(client['pysquad-reservation-system']['Reservation'].find({}))
        
        # (Optional) Process or combine data from MongoDB if needed
    except ConnectionFailure:
        db_status = "MongoDB connection failed"
        mongo_reservations = []

    return render(request, 'reservations/view_reservations.html', {
        'reservations': reservations,
        'db_status': db_status,
        'mongo_reservations': mongo_reservations,  # Include data from MongoDB
    })