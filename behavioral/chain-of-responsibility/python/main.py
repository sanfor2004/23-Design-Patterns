class Request:
    def __init__(self, authenticated, amount_cents):
        self.authenticated = authenticated
        self.amount_cents = amount_cents


class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def accepts(self, request):
        raise NotImplementedError

    def handle(self, request):
        if not self.accepts(request):
            return False
        if self.next_handler is None:
            return True
        return self.next_handler.handle(request)


class Auth(Handler):
    def accepts(self, request):
        return request.authenticated


class Limit(Handler):
    def accepts(self, request):
        return 0 < request.amount_cents <= 10000


if __name__ == "__main__":
    chain = Auth(Limit())
    for authenticated, amount_cents in [(False, 2000), (True, 20000),
                                       (True, 2000), (True, 0), (True, 10000)]:
        request = Request(authenticated, amount_cents)
        print("Accepted" if chain.handle(request) else "Rejected")
