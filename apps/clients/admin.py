from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'company_name', 'document', 'email')
