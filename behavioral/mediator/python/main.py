class Field:
    def __init__(self, changed):
        self.changed = changed
        self.value = ""

    def set(self, value):
        self.value = value
        self.changed()


class Button:
    def __init__(self):
        self.enabled = False


class LoginForm:
    def __init__(self):
        self.username = Field(self.changed)
        self.password = Field(self.changed)
        self.submit = Button()

    def changed(self):
        self.submit.enabled = bool(self.username.value and self.password.value)


if __name__ == "__main__":
    form = LoginForm()
    form.username.set("learner")
    print("Ready:", form.submit.enabled)
    form.password.set("example")
    print("Ready:", form.submit.enabled)
    form.password.set("")
    print("Ready:", form.submit.enabled)
