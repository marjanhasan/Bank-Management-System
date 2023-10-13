from abc import ABC, abstractmethod


class Account(ABC):
    accounts = []

    def __init__(self, name, email, address, account_type) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_no = len(self.accounts) + 21
        Account.accounts.append(self)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: ${amount}. New Balance: ${self.balance}")
        elif amount > self.balance:
            print(f"Withdrawal amount exceeded")
        else:
            print(f"Invalid amount request. Please Try again!")
