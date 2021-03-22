from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField("Code", max_length=50, unique=True)
    coupon_start = models.DateTimeField("start_of_coupon")
    coupon_finish = models.DateTimeField("finish_of_coupon",)
    discount = models.IntegerField("Discovery", validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField("Active", default=False)

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return self.code
