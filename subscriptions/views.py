from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import ServiceUser, Service, Subscription
from .forms import SubscriptionForm

class ServiceUserListView(ListView):
    model = ServiceUser
    template_name = 'subscriptions/serviceuser_list.html'
    context_object_name = 'users'

class ServiceUserDetailView(DetailView):
    model = ServiceUser
    template_name = 'subscriptions/serviceuser_detail.html'
    context_object_name = 'user'

class ServiceListView(ListView):
    model = Service
    template_name = 'subscriptions/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'subscriptions/service_detail.html'
    context_object_name = 'service'
    slug_field = 'type'
    slug_url_kwarg = 'type'

    def get_object(self):
        return get_object_or_404(Service, type=self.kwargs['type'])
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        subscriptions = service.subscription_set.all()
        for subscription in subscriptions:
            print(subscription.date_created)  # Debug print statement
        context['subscriptions'] = subscriptions
        return context

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscriptions/create_subscription.html'
    success_url = reverse_lazy('subscription_list')

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions})


# class SubscriptionListView(ListView):
#     model = Subscription
#     template_name = 'subscriptions/subscription_list.html'
#     context_object_name = 'subscriptions'
