from django.contrib import admin
from .models import MaintenanceContract

@admin.register(MaintenanceContract)
class MaintenanceContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'project', 'monthly_value', 'next_billing_date', 'active')
    list_filter = ('active',)
