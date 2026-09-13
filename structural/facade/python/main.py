class Stock:
    def available(self, quantity):
        return 0 < quantity <= 3


class Payment:
    def charge(self, amount_cents):
        print("Charged", amount_cents, "cents")


class Shipping:
    def dispatch(self):
        print("Dispatched")


class Checkout:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.shipping = Shipping()

    def buy(self, quantity):
        if not self.stock.available(quantity):
            return False
        self.payment.charge(quantity * 1000)
        self.shipping.dispatch()
        return True


if __name__ == "__main__":
    checkout = Checkout()
    checkout.buy(2)
    if not checkout.buy(4):
        print("Unavailable")
    if not checkout.buy(0):
        print("Invalid quantity")
