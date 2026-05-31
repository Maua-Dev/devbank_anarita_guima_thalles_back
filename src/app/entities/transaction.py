from datetime import datetime

class Transaction:
    def __init__(self, type: str, value: float):
        if type not in ["DEPOSIT", "WITHDRAW"]:
            raise ValueError("Tipo de transação inválido!!")
        if value <= 0:
            raise ValueError("Valor da transação inválido!!")

        self.type = type
        self.value = value
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "timestamp": self.timestamp.isoformat()
        }
