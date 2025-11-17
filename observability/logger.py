class Logger:
    def info(self, message, **data):
        print("[INFO]", message, data)

logger = Logger()
