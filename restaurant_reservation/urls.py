from django.urls import path
from reservations import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('manage/<int:reservation_id>/', views.manage_reservation, name='manage_reservation'),
    path('assign/<int:reservation_id>/', views.assign_table, name='assign_table'),
    path('view/', views.view_reservations, name='view_reservations'),
]