from src.app.entities.transaction import Transaction

class User:
#classe usuário é criada com seus devidos atributos (nome, agência, conta e saldo atual)
    def __init__(
        self,
        name: str,
        agency: str,
        account: str,
        current_balance: float = 0
    ):
    #validação dos atributos do usuário
        if name == "":
            raise ValueError("Usuário inválido!!")

        if agency == "":
            raise ValueError("Agência inválida!!")

        if account == "":
            raise ValueError("Conta inválida!!")

        if current_balance < 0:
            raise ValueError("Saldo inválido!!")

        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = current_balance

        self.transactions = []

    #definição e validação dos métodos de depósito e saque
    def deposit(self, value: float):

        if value <= 0:
            raise ValueError("Valor inválido inserido!!")

        self.current_balance += value

        self.transactions.append(
            Transaction(
                transaction_type="deposit",
                value=value,
                current_balance=self.current_balance
            )
        )
        
    

    def withdraw(self, value: float):

        if value <= 0:
            raise ValueError("Valor inválido inserido!!")

        if value > self.current_balance:
            raise ValueError("Saldo insuficiente para transação!!")

        self.current_balance -= value

        self.transactions.append(
            Transaction(
                transaction_type="withdraw",
                value=value,
                current_balance=self.current_balance
            )
        )
   
   
   #retorna os dados do usuário em formato de dicionário json     
    def to_dict(self):

        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }