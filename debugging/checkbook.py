#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            while True:
                try:
                    amt = float(input("Enter the amount to deposit: $"))
                    if amt <= 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.deposit(amt)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")

        elif action == 'withdraw':
            while True:
                try:
                    amt = float(input("Enter the amount to withdraw: $"))
                    if amt <= 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.withdraw(amt)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")

        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
