from django import forms
from .models import ServiceUser, Service, Subscription

class ServiceUserForm(forms.ModelForm):
    class Meta:
        model = ServiceUser
        fields = ['name', 'email', 'age', 'gender']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['type', 'mode_of_payment', 'company']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['user', 'service', 'amount']
