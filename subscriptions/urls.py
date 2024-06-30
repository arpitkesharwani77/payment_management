# subscriptions/urls.py

from django.urls import path
from .views import (
    ServiceUserListView, 
    ServiceUserDetailView, 
    ServiceListView, 
    ServiceDetailView, 
    SubscriptionCreateView,
    subscription_list,
    # SubscriptionListView
)

urlpatterns = [
    path('users/', ServiceUserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', ServiceUserDetailView.as_view(), name='user_detail'),
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<str:type>/', ServiceDetailView.as_view(), name='service_detail'),
    path('subscription/', SubscriptionCreateView.as_view(), name='create_subscription'),
    path('subscriptions_details/', subscription_list, name='subscription_list'),
]
