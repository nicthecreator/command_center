from django.contrib import admin
from .models import HostingAccount

@admin.register(HostingAccount)
class HostingAccountAdmin(admin.ModelAdmin):
    list_display = ('provider', 'plan', 'client', 'project', 'expiration_date', 'status')
    list_filter = ('status', 'billing_cycle')
    search_fields = ('provider', 'server', 'client__name', 'project__name')
