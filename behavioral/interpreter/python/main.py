class Role:
    def __init__(self, name):
        self.name = name

    def evaluate(self, context):
        return self.name in context


class Both:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, context):
        return self.left.evaluate(context) and self.right.evaluate(context)


if __name__ == "__main__":
    rule = Both(Role("editor"), Role("verified"))
    for context in [set(), {"editor"}, {"editor", "verified"}]:
        print(rule.evaluate(context))
