class Transaction:

    def __init__(
        self,
        transaction_type: str,
        value: float,
        current_balance: float
    ):

        self.transaction_type = transaction_type
        self.value = value
        self.current_balance = current_balance

    def to_dict(self):

        return {
            "transaction_type": self.transaction_type,
            "value": self.value,
            "current_balance": self.current_balance
        }