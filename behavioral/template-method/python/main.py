class Report:
    def generate(self):
        print("Begin report")
        data = self.read()
        self.format(data)
        print("End report")

    def read(self):
        raise NotImplementedError

    def format(self, data):
        raise NotImplementedError


class TextReport(Report):
    def read(self):
        return "sales=42"

    def format(self, data):
        print(data)


if __name__ == "__main__":
    TextReport().generate()
