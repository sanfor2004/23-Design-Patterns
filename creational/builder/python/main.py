class Request:
    def __init__(self, endpoint, timeout=30, retry=False):
        self.endpoint = endpoint
        self.timeout = timeout
        self.retry = retry

    def describe(self):
        print(f"{self.endpoint} timeout={self.timeout} retry={self.retry}")


class RequestBuilder:
    def __init__(self):
        self.endpoint_value = ""
        self.timeout_value = 30
        self.retry_value = False

    def endpoint(self, value):
        self.endpoint_value = value
        return self

    def timeout(self, seconds):
        self.timeout_value = seconds
        return self

    def retry(self, enabled):
        self.retry_value = enabled
        return self

    def build(self):
        if not self.endpoint_value or self.timeout_value <= 0:
            raise ValueError("Invalid request")
        return Request(self.endpoint_value, self.timeout_value, self.retry_value)


def main():
    RequestBuilder().endpoint("/orders").timeout(5).retry(True).build().describe()
    try:
        RequestBuilder().build()
    except ValueError:
        print("Invalid request rejected")
    try:
        RequestBuilder().endpoint("/orders").timeout(0).build()
    except ValueError:
        print("Zero timeout rejected")


if __name__ == "__main__":
    main()
