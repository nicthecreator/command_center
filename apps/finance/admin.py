from django.contrib import admin
from .models import Sale, Payment

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'project', 'amount', 'sale_date', 'status')
    list_filter = ('status',)
    inlines = [PaymentInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'amount', 'payment_date', 'payment_method', 'status')
    list_filter = ('status', 'payment_method')
