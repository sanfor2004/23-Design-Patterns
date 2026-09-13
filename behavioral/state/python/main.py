class Closed:
    name = "closed"

    def press(self, door):
        door.state = Open()


class Open:
    name = "open"

    def press(self, door):
        door.state = Closed()


class Door:
    def __init__(self):
        self.state = Closed()

    def press(self):
        self.state.press(self)


if __name__ == "__main__":
    door = Door()
    print(door.state.name)
    door.press()
    print(door.state.name)
    door.press()
    print(door.state.name)
