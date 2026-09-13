class Checkout:
    def __init__(self, shipping_rule):
        self.shipping_rule = shipping_rule

    def total(self, subtotal_cents):
        if subtotal_cents < 0:
            raise ValueError("Negative subtotal")
        return subtotal_cents + self.shipping_rule(subtotal_cents)


def standard(subtotal_cents):
    return 500


def express(subtotal_cents):
    return 0 if subtotal_cents >= 10000 else 1500


def main():
    print("Standard:", Checkout(standard).total(4000))
    print("Express:", Checkout(express).total(4000))
    print("Express boundary:", Checkout(express).total(10000))
    try:
        Checkout(standard).total(-1)
    except ValueError:
        print("Negative subtotal rejected")


if __name__ == "__main__":
    main()
