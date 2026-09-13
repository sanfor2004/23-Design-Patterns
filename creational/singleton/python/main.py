class Metrics:
    def __init__(self):
        self.requests = 0

    def record(self):
        self.requests += 1


# One shared instance under normal imports of this module.
# This expresses shared access, not a ban on creating other Metrics objects.
metrics = Metrics()


def main():
    first = metrics
    second = metrics
    first.record()
    second.record()
    print("Same instance:", first is second)
    print("Requests:", metrics.requests)


if __name__ == "__main__":
    main()
