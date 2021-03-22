
from django import forms


class CouponApplyForm(forms.Form):
    """Form addle coupon"""
    code = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-10 mr-10", "id": "inputfname", "placeholder": "Coupon Code"}))