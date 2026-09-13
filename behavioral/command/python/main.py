class Document:
    def __init__(self, text):
        self.text = text


class Append:
    def __init__(self, document, suffix):
        self.document = document
        self.suffix = suffix
        self.before = None

    def execute(self):
        self.before = self.document.text
        self.document.text += self.suffix

    def undo(self):
        self.document.text = self.before


class History:
    def __init__(self):
        self.commands = []

    def run(self, command):
        command.execute()
        self.commands.append(command)

    def undo(self):
        if self.commands:
            self.commands.pop().undo()


if __name__ == "__main__":
    document = Document("Hello")
    history = History()
    history.run(Append(document, " world"))
    history.run(Append(document, "!"))
    print(document.text)
    for _ in range(3):
        history.undo()
        print(document.text)
