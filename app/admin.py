from django.contrib import admin
from .models import Rental, Reservation

admin.site.register([Rental, Reservation])
