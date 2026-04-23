class BankAccount:

    def __init__(self, owner: str , balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance


    def deposit(self, amount:float ) -> None:
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited {amount}. Balance is {self.balance}")
        else:
            print("Error: Wrong amount")

    def withdraw(self, amount:float) -> None:
        if self.balance > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Balance is {self.balance}")
        else:
            print("Not enough money")

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Account: {self.owner}, balance: {self.balance}"

    def operation(self) -> None:

        while True:
            print(
                "---------Choose operation-------------\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Show Account\n5. Exit")
            op = input("Enter your choice: ")

            match op:
                case "1":
                    try:
                        amount = float(input("Enter amount: "))
                        self.deposit(amount)
                    except ValueError:
                        print("Error: Enter numbers, mot words")
                case "2":
                    try:
                        amount = float(input("Enter amount: "))
                        self.withdraw(amount)
                    except ValueError:
                        print("Error: Enter numbers, mot words")
                case "3":
                    print(self.get_balance())
                case "4":
                    print(self)
                case "5":
                    exit()
                case _:
                    print("Error: Wrong operation")



if __name__ == "__main__":

    acc = {"tom":BankAccount("tom",2000), "max": BankAccount("max",3400)}
    print("--------Welcome to Bank Account.-----------")
    name = str(input("Enter your name: "))


    if name in acc:
        user_acc = acc[name]
        user_acc.operation()
    elif name not in acc:
        try:
            balance = float(input("Enter your balance: "))
            new_acc = BankAccount(name, balance)
            acc[name] = new_acc
            new_acc.operation()
        except ValueError :
            print("Error: Balance is numbers")

    else:
        print("Error")


