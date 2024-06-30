
from django.contrib import admin
from .models import ServiceUser, Service, Subscription

class ServiceUserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_filter = ['gender']

admin.site.register(ServiceUser, ServiceUserAdmin)
admin.site.register(Service)
admin.site.register(Subscription)
