class Book:
    def __init__(self, price_cents):
        self.price_cents = price_cents

    def accept(self, visitor):
        visitor.visit_book(self)


class Food:
    def __init__(self, price_cents):
        self.price_cents = price_cents

    def accept(self, visitor):
        visitor.visit_food(self)


class Tax:
    def __init__(self):
        self.total_cents = 0

    def visit_book(self, book):
        self.total_cents += book.price_cents // 10

    def visit_food(self, food):
        self.total_cents += food.price_cents // 5


def tax_cents(basket):
    tax = Tax()
    for item in basket:
        item.accept(tax)
    return tax.total_cents


if __name__ == "__main__":
    print("Tax:", tax_cents([Book(2000), Food(1000)]), "cents")
    print("Empty basket tax:", tax_cents([]), "cents")
