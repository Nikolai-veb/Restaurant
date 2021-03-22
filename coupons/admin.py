from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'coupon_start', 'coupon_finish', 'discount', 'active')
    list_filter = ('active', 'coupon_start', 'coupon_finish')
    list_display_links = ('id', 'code')
    list_editable = ('active',)
    search_fields = ('code',)
