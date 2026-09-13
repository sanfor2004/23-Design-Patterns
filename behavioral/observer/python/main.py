class Stock:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def set(self, quantity):
        for listener in self.listeners.copy():
            listener(quantity)


def screen(quantity):
    print("Screen:", quantity)


def log(quantity):
    print("Log:", quantity)


def main():
    stock = Stock()
    stock.subscribe(screen)
    stock.subscribe(log)
    stock.set(4)
    stock.unsubscribe(screen)
    stock.set(0)
    stock.unsubscribe(log)
    stock.set(8)
    print("No subscribers")


if __name__ == "__main__":
    main()
