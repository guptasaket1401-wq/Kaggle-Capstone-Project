class MemoryBank:
    def __init__(self):
        self.storage = {
            "EnterpriseKnowledge": "Use corporate tone, emphasize KPIs and insights."
        }

    def get(self, key):
        return self.storage.get(key, "")
