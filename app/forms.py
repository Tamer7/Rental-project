from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = '__all__'
