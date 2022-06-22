from django.test import TestCase
from datetime import date
from .models import Reservation, Rental


class ReservationsTests(TestCase):
    def test_creating_rental(self):
        rental = Rental.objects.create(name="test 1")

        self.assertEqual(rental.id, 1)
        self.assertEqual(rental.name, 'test 1')

    def test_creating_reservation(self):
        rental = Rental.objects.create(name="test 1")
        checkin = date(2022, 1, 1)
        checkout = date(2022, 2, 2)
        reservation = Reservation.objects.create(
            rental=rental, checkin=checkin, checkout=checkout)

        self.assertEqual(reservation.rental.id, rental.id)
        self.assertEqual(reservation.rental.name, 'test 1')
        self.assertEqual(reservation.checkin, checkin)
        self.assertEqual(reservation.checkout, checkout)

    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
