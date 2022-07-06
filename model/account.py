class Account:
    def __init__(self, a_id, account, balance, customer_id):
        self.id = a_id
        self.account = account
        self.balance = balance
        self.customer_id = customer_id

    def to_dict(self):
        return{
            "id": self.id,
            "account" : self.account,
            "balance": self.balance,
            "customer_id" : self.customer_id

        }