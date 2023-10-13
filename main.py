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
