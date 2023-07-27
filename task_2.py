# Розробіть клас BankAccount для представлення банківського рахунку.
# Додайте методи для зняття та поповнення коштів на рахунку.
# Використовуйте магічний метод __str__ для виведення інформації про рахунок.


def task_2():

    class BankAccount:

        def __init__(self, account_number, account_holder, balance=0):
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = balance

        def deposit(self, amount):
            """Method for replenishing funds on the account."""
            if amount > 0:
                self.balance += amount
                return True
            else:
                print("Invalid deposit amount. Please deposit a positive value.")
                return False

        def withdraw(self, amount):
            """Method for withdrawing funds from the account."""
            if 0 < amount <= self.balance:
                self.balance -= amount
                return True
            else:
                print("Insufficient funds. Unable to withdraw.")
                return False

        def get_balance(self):
            """A method for obtaining the current account balance."""
            return self.balance

        def __str__(self):
            """A method that returns a string with account information."""
            return f"Account Holder: {self.account_holder}\nAccount Number: " \
                   f"{self.account_number}\nBalance: {self.balance}"

    person_1 = BankAccount(1, "Maksim", 1000)
    person_2 = BankAccount(2, "Vadim", 400)
    person_3 = BankAccount(3, "Mike", 500)

    print(BankAccount.__str__(person_1))
    print(BankAccount.__str__(person_2))
    print(BankAccount.__str__(person_3))

    print("------------------------------")

    BankAccount.deposit(person_3, 770)
    BankAccount.deposit(person_1, 3000)
    BankAccount.withdraw(person_2, 200)

    print(BankAccount.__str__(person_1))
    print(BankAccount.__str__(person_2))
    print(BankAccount.__str__(person_3))
