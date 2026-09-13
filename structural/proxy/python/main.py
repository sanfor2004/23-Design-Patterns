class DiskImage:
    def __init__(self):
        print("Load image")

    def display(self):
        print("Display image")


class LazyImage:
    def __init__(self):
        self.image = None

    def display(self):
        if self.image is None:
            self.image = DiskImage()
        self.image.display()


if __name__ == "__main__":
    image = LazyImage()
    print("Proxy ready")
    image.display()
    image.display()
