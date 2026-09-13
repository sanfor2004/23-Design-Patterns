class Button:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " button"


class Panel:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " panel"


class DarkTheme:
    def button(self):
        return Button("dark")

    def panel(self):
        return Panel("dark")


class LightTheme:
    def button(self):
        return Button("light")

    def panel(self):
        return Panel("light")


def render(theme):
    print(theme.button().paint() + " + " + theme.panel().paint())


if __name__ == "__main__":
    render(DarkTheme())
    render(LightTheme())
