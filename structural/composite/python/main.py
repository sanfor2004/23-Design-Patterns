class File:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Negative size")
        self.size = size

    def bytes(self):
        return self.size


class Folder:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def bytes(self):
        return sum(child.bytes() for child in self.children)


def main():
    root = Folder()
    print("Empty:", root.bytes(), "bytes")
    images = Folder()
    images.add(File(20))
    root.add(File(10))
    root.add(images)
    print("Total:", root.bytes(), "bytes")
    try:
        File(-1)
    except ValueError:
        print("Negative size rejected")


if __name__ == "__main__":
    main()
