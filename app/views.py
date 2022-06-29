from django.views.generic import CreateView
from .models import Reservation
from .forms import ReservationForm


class HomeView(CreateView):
    template_name = "index.html"
    form_class = ReservationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.all(
        ).select_related('rental')
        return context
