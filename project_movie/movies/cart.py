class SessionCart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product_id):
        self.cart[str(product_id)] = self.cart.get(str(product_id), 0) + 1
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product_id):
        self.cart.pop(str(product_id), None)
        self.session['cart'] = self.cart
        self.session.modified = True

    def items(self):
        return self.cart