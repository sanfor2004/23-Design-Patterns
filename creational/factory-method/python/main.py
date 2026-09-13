class EmailSender:
    def send(self, message):
        print("Email:", message)


class ConsoleSender:
    def send(self, message):
        print("Console:", message)


class AlertJob:
    def make_sender(self):
        raise NotImplementedError

    def run(self):
        sender = self.make_sender()
        sender.send("build complete")


class EmailJob(AlertJob):
    def make_sender(self):
        return EmailSender()


class ConsoleJob(AlertJob):
    def make_sender(self):
        return ConsoleSender()


if __name__ == "__main__":
    EmailJob().run()
    ConsoleJob().run()
