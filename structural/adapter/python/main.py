class LegacyThermometer:
    def fahrenheit(self):
        return 77.0


class CelsiusAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def celsius(self):
        return (self.sensor.fahrenheit() - 32) * 5 / 9


def display(temperature):
    print(temperature.celsius(), "C")


if __name__ == "__main__":
    display(CelsiusAdapter(LegacyThermometer()))
