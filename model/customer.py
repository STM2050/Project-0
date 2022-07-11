class Customer:
    def __init__(self, customer_id, customername, active):
        self.id = customer_id
        self.customername = customername
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "customername": self.customername,
            "active": self.active
        }