from dataclasses import dataclass


@dataclass(frozen=True)
class Glyph:
    shape: str


class GlyphPool:
    def __init__(self):
        self.glyphs = {}

    def get(self, symbol):
        if symbol not in self.glyphs:
            self.glyphs[symbol] = Glyph(symbol)
        return self.glyphs[symbol]


class PlacedGlyph:
    def __init__(self, glyph, x):
        self.glyph = glyph
        self.x = x

    def draw(self):
        print(self.glyph.shape, "at", self.x)


if __name__ == "__main__":
    pool = GlyphPool()
    first = PlacedGlyph(pool.get("A"), 0)
    second = PlacedGlyph(pool.get("A"), 10)
    first.draw()
    second.draw()
    print("Shared shape:", first.glyph is second.glyph)
    print("Different shape:", first.glyph is pool.get("B"))
