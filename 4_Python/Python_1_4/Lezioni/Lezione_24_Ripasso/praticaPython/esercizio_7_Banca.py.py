# 7
'''Progettare un semplice sistema bancario con i seguenti requisiti:
    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.'''

class Account:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Invalid amount")  # inglese

    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: str):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")  # inglese
        account = Account(account_id)
        self.accounts[account_id] = account
        return account

    def deposit(self, account_id: str, amount: float):
        if account_id not in self.accounts:
            raise ValueError("Account not found")  # inglese
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str) -> float:
        if account_id not in self.accounts:
            raise ValueError("Account not found")  # inglese
        return self.accounts[account_id].get_balance()

bank = Bank()                           # 0
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()                           # 100
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()                           # 200
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))
