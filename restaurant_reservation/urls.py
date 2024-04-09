from django.urls import path
from ..reservations import views

urlpatterns = [
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('manage_reservation/<int:reservation_id>/', views.manage_reservation, name='manage_reservation'),
    path('assign_table/<int:reservation_id>/', views.assign_table, name='assign_table'),
]