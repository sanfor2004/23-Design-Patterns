class Snapshot:
    def __init__(self, text):
        self._text = text


class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text = text

    def save(self):
        return Snapshot(self.text)

    def restore(self, snapshot):
        self.text = snapshot._text


if __name__ == "__main__":
    editor = Editor()
    editor.write("Draft")
    checkpoint = editor.save()
    editor.write("Broken edit")
    print(editor.text)
    editor.restore(checkpoint)
    print(editor.text)
    editor.write("Another edit")
    editor.restore(checkpoint)
    print(editor.text)
