from .cart import Cart


def cart(request):
    cart = Cart(request)
    cart_little = cart.inter()[:2]
    return {'cart': cart, 'cart_little': cart_little}
