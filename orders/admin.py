from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'email', 'pained', 'created']
    list_filter = ['pained', 'created', 'update', 'city']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name', 'last_name', 'email', 'city', 'address', 'postal_code']
    list_editable = ("pained",)
    inlines = [OrderItemInline]