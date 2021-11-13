

def get_amount_cart(request):
    cart=request.session['cart'] if request.session['cart'] else {}
    amount_cart = len(cart)
    return {
        'amount_cart': amount_cart,
    }