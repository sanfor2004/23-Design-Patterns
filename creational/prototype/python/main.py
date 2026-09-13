class Guard:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment

    def clone(self):
        return Guard(self.name, self.equipment.copy())

    def describe(self):
        print(self.name + ": " + ", ".join(self.equipment))


def main():
    prototype = Guard("template", ["shield", "spear"])
    guard = prototype.clone()
    guard.name = "gate guard"
    guard.equipment.append("helmet")
    prototype.describe()
    guard.describe()


if __name__ == "__main__":
    main()
