class Metrics:
    def __init__(self):
        self.data = {}

    def increment(self, key, amount=1):
        self.data[key] = self.data.get(key, 0) + amount

metrics = Metrics()
