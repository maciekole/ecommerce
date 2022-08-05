from cart.models.cart import Cart


def cart(request):
    return {'cart': Cart(request)}
