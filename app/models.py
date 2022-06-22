from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(
        Rental, on_delete=models.CASCADE, related_name="reservations")
    checkin = models.DateField()
    checkout = models.DateField()

    def get_previous_reservation(self):
        latest_reservation = Reservation.objects.order_by('-checkout').filter(
            rental=self.rental, checkout__lt=self.checkout).first()
        if latest_reservation is not None:
            return latest_reservation.id
        return '-'

    def __str__(self):
        return f"({self.id}, {self.checkin}, {self.checkout})"
