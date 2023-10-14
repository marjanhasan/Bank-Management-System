import random


class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.bankrupt = False
        self.loan_system = True


class User:
    def __init__(self, name, email, address, account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.balance = 0
        self.account_no = random.randint(10000, 100000)
        self.transaction_history = []
        self.loan_times = 0

    def password(self, password):
        self.password = password

    def deposite(self, bank, amount):
        if bank.bankrupt == False:
            if amount > 0:
                self.bank = bank
                self.balance += amount
                self.bank.total_balance += amount
                history = f"\n-->Successfully deposited: ${amount}. New Balance: ${self.balance}\n"
                self.transaction_history.append(history)
                print(history)
            else:
                print(f"\n-->Invalid deposit amount. Please Try again!\n")
        else:
            print("\n-->The bank is bankrupt, you cann't deposit money\n")

    def withdraw(self, bank, amount):
        if bank.bankrupt == False:
            if amount > 0 and amount <= self.balance:
                self.bank = bank
                self.balance -= amount
                self.bank.total_balance -= amount
                history = f"\n-->Withdraw: ${amount}. New Balance: ${self.balance}\n"
                self.transaction_history.append(history)
                print(history)
            elif amount > self.balance:
                print(f"\n-->Withdrawal amount exceeded\n")
            else:
                print(f"\n-->Invalid amount request. Please Try again!\n")
        else:
            print(f"\n-->The bank is bankrupt, you cann't withdraw money\n")

    def show_balance(self):
        print(f"\n-->Your current balance is: ${self.balance}\n")

    def show_transaction_history(self):
        if len(self.transaction_history) > 0:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("\n-->There is no transaction history.\n")

    def take_loan(self, bank, amount):
        self.bank = bank
        if self.bank.bankrupt == False:
            if self.bank.loan_system == True:
                if self.loan_times < 2:
                    self.balance += amount
                    self.bank.total_balance -= amount
                    self.bank.total_loan += amount
                    history = f"\n-->Loan issued successfully and ${amount} added\n"
                    self.transaction_history.append(history)
                    self.loan_times += 1
                    print(history)
                else:
                    print("\n-->Sorry! You cann't take loan more than 2 times.\n")
            else:
                print(f"\n-->The bank loan system is turned off\n")
        else:
            print(f"\n-->The bank is bankrupt, you cann't take loan\n")

    def transfer_money(self, bank, amount, user_name):
        self.bank = bank
        if len(self.bank.users) >= 2:
            for user in self.bank.users:
                if user_name == user.name:
                    if self.balance >= amount:
                        user.balance += amount
                        self.balance -= amount
                        history = f"\n-->Balance successfully transferred to {user_name} from {self.name}, and the amount is {amount}\n"
                        self.transaction_history.append(history)
                        print(history)
                        return
                    else:
                        print(f"\n-->Transaction amount exceed\n")
                        return
            else:
                print(f"\n-->Username {user_name} doesn't exists.\n")
        else:
            print(f"\n-->Oops! There are few user.\n")


class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.name = "admin"
        self.password = "1234"

    def show_users(self):
        if len(self.bank.users) > 0:
            print(f"\n-->Available users down below\n")
            for user in self.bank.users:
                print(
                    f"-->Name: {user.name}, Account No: {user.account_no}, Email: {user.email}, Address: {user.address}, Account Type: {user.account_type}"
                )
                print()
        else:
            print(f"\n-->No user found.\n")

    def check_bank_balance(self):
        print(
            f"\n-->Total balance of {self.bank.name} bank is ${self.bank.total_balance}\n"
        )

    def check_bank_loan(self):
        print(f"\n-->Total loan of {self.bank.name} bank is ${self.bank.total_loan}\n")

    def loan_system_status(self, status):
        if status == "1":
            self.bank.loan_system = True
            print(f"\n-->The loan system is turned on!\n")
        elif status == "2":
            self.bank.loan_system = False
            print(f"\n-->The loan system is turned off!\n")
        else:
            print(f"\n-->Oops! Invalid key status. Please try again!\n")

    def bankrupt_status(self, status):
        if status == "1":
            self.bank.bankrupt = True
            print(f"\n-->{self.bank.name} bank successfully bankrupted by the admin\n")
        elif status == "2":
            self.bank.bankrupt = False
            print(f"\n-->{self.bank.name} is successfully opened by admin!\n")
        else:
            print(f"\n-->Oops! Invalid key status. Please try again!\n")

    def delete_user(self, email):
        for user in self.bank.users:
            if user.email == email:
                self.bank.users.remove(user)
                print(f"\n-->{user.name} deleted successfully\n")
                return
        print("\n-->User not found!\n")


class Authentication:
    def __init__(self) -> None:
        self.logged_in = None

    def Registration(self, bank, user):
        self.bank = bank
        self.user = user
        for users in bank.users:
            if self.user.email == users.email:
                print(f"\n-->Already Registered!\n")
                return
        self.bank.users.append(self.user)
        print(f"\n-->{self.user.name} registered successfully!\n")

    def login(self, bank, email, password):
        self.bank = bank
        for user in self.bank.users:
            if user.email == email and user.password == password:
                self.logged_in = user
                print(f"\n-->{user.name} successfully logged in!\n")
                return True
        print("\n-->Oops! Invalid email or password. Please try agian!\n")

    def log_out(self):
        self.logged_in = None


dbbl = Bank("DBBL", "Dhaka")
admin = Admin(dbbl)
register = Authentication()

while True:
    print(f"\n-->Welcome to the {dbbl.name} bank\n")
    print("-->Admin/User")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    option = input("Enter option:")

    if option == "1":
        print("\nLogin as Admin")
        user_name = input("\nEnter admin name:")
        password = input("\nEnter admin password:")
        if user_name == admin.name and password == admin.password:
            print("\n-->Successfully logged in\n")
            while True:
                print("1. Create account for user")
                print("2. Show all user accounts")
                print("3. Show total available balance")
                print("4. Show total loan amount")
                print("5. Delete user account")
                print("6. Turn on/off loan system")
                print("7. Turn on/off bankrupt system")
                print("8. Log Out")
                option = input("\nEnter option:")

                if option == "1":
                    name = input("\nEnter user name:")
                    email = input("Enter user email:")
                    address = input("Enter user address:")
                    account_type = input(
                        "Enter '1' for 'Savings' type or Enter '2' for 'Current' type account"
                    )
                    password = input("enter user password:")
                    if account_type == "1":
                        new_user = User(name, email, address, "Savings", password)
                    elif account_type == "2":
                        new_user = User(name, email, address, "Current", password)
                    else:
                        print("\n-->Oops! Invalid account type. Please Try again!\n")
                    register.Registration(dbbl, new_user)
                elif option == "2":
                    admin.show_users()
                elif option == "3":
                    admin.check_bank_balance()
                elif option == "4":
                    admin.check_bank_loan()
                elif option == "5":
                    email = input("\nEnter email:")
                    admin.delete_user(email)
                elif option == "6":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    admin.loan_system_status(option)
                elif option == "7":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    admin.bankrupt_status(option)
                elif option == "8":
                    break
                else:
                    print("\nOops! Invalid selection. Please try again!\n")
        else:
            print("\n-->Oops! Invalid name or password. Please Try again!")
    elif option == "2":
        if len(dbbl.users) > 0:
            print("\nLogin as User")
            user_email = input("Enter user email:")
            password = input("Enter password:")
            log_in = register.login(dbbl, user_email, password)
            if log_in:
                while True:
                    print("1. Show Balance")
                    print("2. Deposite Money")
                    print("3. Withdraw Money")
                    print("4. Transfer Money")
                    print("5. Transaction History")
                    print("6. Take Loan")
                    print("7. Log Out")
                    option = input("\nEnter Option:")
                    user = register.logged_in

                    if option == "1":
                        user.show_balance()
                    elif option == "2":
                        amount = int(input("\nEnter amount:"))
                        user.deposite(dbbl, amount)
                    elif option == "3":
                        amount = int(input("\nEnter amount:"))
                        user.withdraw(dbbl, amount)
                    elif option == "4":
                        name = input("\nEnter name of receiver:")
                        amount = int(input("\nEnter amount:"))
                        user.transfer_money(dbbl, amount, name)
                    elif option == "5":
                        user.show_transaction_history()
                    elif option == "6":
                        amount = int(input("\nEnter loan amount:"))
                        user.take_loan(dbbl, amount)
                    elif option == "7":
                        register.log_out()
                        break
                    else:
                        print("\nOops! Invalid options. Please Try again!\n")
            else:
                print("\nNo Login User. Please Try again!\n")
        else:
            print("\nThere are no user. Please contact with admin\n")
    elif option == "3":
        break
    else:
        print("\nOops! Invalid Selection. Please Try again!\n")
