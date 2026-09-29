from django.contrib import admin
from .models import Domain

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'client', 'project', 'expiration_date', 'status', 'auto_renew')
    list_filter = ('status', 'auto_renew')
    search_fields = ('domain', 'registrar', 'client__name', 'project__name')
