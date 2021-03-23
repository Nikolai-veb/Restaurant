from django.db import models
from shop.models import Products
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon


class Order(models.Model):
    """Заказ"""
    first_name = models.CharField("Name", max_length=50)
    last_name = models.CharField("Familiya", max_length=50)
    email = models.EmailField("Email")
    city = models.CharField("City", max_length=50)
    address = models.CharField("Address", max_length=250)
    postal_code = models.CharField("Postal code", max_length=20)
    pained = models.BooleanField("Pained", default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    coupon = models.ForeignKey(Coupon, verbose_name="Coupon", null=True, blank=True, related_name="orders", on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created"]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.item.all())
        return total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    """Наменклатура заказа"""
    order = models.ForeignKey(Order, verbose_name="Order", related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name="Product", related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Quantity", default=0)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        cost = self.price * self.quantity
        return cost