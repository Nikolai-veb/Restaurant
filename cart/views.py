from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from shop.models import Products
from .cart import Cart
from .forms import CartAddProductForm
#from couponss.forms import CouponApplyForm


@require_POST
def cart_add(request, prod_id):
    """Oбработчик для добавления товаров в корзину"""
    cart = Cart(request)
    product = get_object_or_404(Products, id=prod_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, prod_id):
    """Обработчик для удаления товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Products, id=prod_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    """Oбработчик для страницы списка товаров, добавленных в корзину"""
    cart = Cart(request)
    for item in cart.inter():
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )
    #coupon_apply_form = CouponApplyForm
    return render(request, 'cart/cart_detail.html', {'cart': cart})
