from django.urls import reverse
from django.shortcuts import render, redirect
from orders.models.item import OrderItem
from orders.forms.order_form import OrderCreateForm
from cart.models.cart import Cart
from orders.tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            order.total_price = cart.get_total_price()
            order.save()
            cart.clear()
            # launch async task
            order_created.delay(order.id)
            # return render(request, 'orders/order/created.html', {'order': order})
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
