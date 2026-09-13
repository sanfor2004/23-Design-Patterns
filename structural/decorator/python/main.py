class Coffee:
    def description(self):
        return "coffee"

    def price_cents(self):
        return 1000


class Milk:
    def __init__(self, inner):
        self.inner = inner

    def description(self):
        return self.inner.description() + " + milk"

    def price_cents(self):
        return self.inner.price_cents() + 200


if __name__ == "__main__":
    drink = Milk(Milk(Coffee()))
    print(f"{drink.description()}: {drink.price_cents()} cents")
