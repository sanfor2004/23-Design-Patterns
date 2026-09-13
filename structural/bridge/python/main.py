class Email:
    def deliver(self, text):
        print("Email:", text)


class Sms:
    def deliver(self, text):
        print("SMS:", text)


class Notice:
    def __init__(self, channel):
        self.channel = channel

    def send(self):
        self.channel.deliver("status normal")


class UrgentNotice(Notice):
    def send(self):
        self.channel.deliver("URGENT: disk full")


if __name__ == "__main__":
    Notice(Email()).send()
    UrgentNotice(Email()).send()
    UrgentNotice(Sms()).send()
