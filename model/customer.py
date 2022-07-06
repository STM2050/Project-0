class Customer:
    def __init__(self, id, customername, active):
        self.id = id
        self.customername = customername
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "customername": self.customername,
            "active": self.active
        }