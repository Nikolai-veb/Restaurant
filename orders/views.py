from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
#from .service import send
#from .tasks import send_spam_email


def order_create(request):
    """Обработчик заказов"""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart.inter():
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            var = [iteam for iteam in cart.inter()]
            hand = f"Django Shop"
            body = f"Your Order \n {var[0]['product']}. \n Quantity : {var[0]['quantity']} \n Total price : ${float(var[0]['total_price'])}"
            cd = form.cleaned_data
            #send_spam_email.delay(cd['email'])
            #send(hand, body, cd['email'])
            # Очищаем корзину
            cart.clear()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreatedForm()
        return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})