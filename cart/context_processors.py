

def get_amount_cart(request):
    cart=request.session.get('cart') if request.session.get('cart') else {}
    amount_cart = len(cart)
    return {
        'amount_cart': amount_cart,
    }