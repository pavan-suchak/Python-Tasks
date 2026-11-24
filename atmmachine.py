import random

class ATMSystem:

    def __init__(self):
        self.banks = {}
        self.users = {}
        self.atms = {}
        self.history = {}

        self.single_limit = 10000
        self.session_limit = 25000
        self.transaction_limit = 5


    def add_bank(self):
        name = input("Enter Bank Name: ")
        bank_id = max(self.banks.keys(), default=0) + 1

        self.banks[bank_id] = name
        print("Bank Added Successfully!")

    def view_banks(self):
        for i, name in self.banks.items():
            print(i, name)

    def update_bank(self):
        self.view_banks()
        bank_id = int(input("Enter Bank ID: "))

        if bank_id in self.banks:
            self.banks[bank_id] = input("Enter New Name: ")
            print("Bank Updated!")
        else:
            print("Bank Not Found!")

    def delete_bank(self):
        self.view_banks()
        bank_id = int(input("Enter Bank ID: "))

        if bank_id not in self.banks:
            print("Bank Not Found!")
            return

        if any(u["bank"] == bank_id for u in self.users.values()):
            print("Bank has registered users!")
            return

        if any(a["bank"] == bank_id for a in self.atms.values()):
            print("Bank has registered ATMs!")
            return

        del self.banks[bank_id]
        print("Bank Deleted!")


    def add_user(self):
        if not self.banks:
            print("Add a bank first!")
            return

        name = input("Enter User Name: ")
        self.view_banks()
        bank = int(input("Select Bank ID: "))

        if bank not in self.banks:
            print("Invalid Bank!")
            return

        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            print("Invalid Balance!")
            return

        card = random.randint(1000000000, 9999999999)

        while card in self.users:
            card = random.randint(1000000000, 9999999999)

        pin = random.randint(1000, 9999)

        self.users[card] = {
            "name": name,
            "pin": pin,
            "bank": bank,
            "balance": balance,
            "withdrawn": 0,
            "count": 0
        }

        self.history[card] = []

        print("\nUser Registered Successfully!")
        print("Card Number:", card)
        print("PIN:", pin)

    def view_users(self):
        for card, user in self.users.items():
            print("\nCard:", card)
            print(user)

    def update_user(self):
        card = int(input("Enter Card Number: "))

        if card not in self.users:
            print("User Not Found!")
            return

        user = self.users[card]

        print("1. Update Name")
        print("2. Update PIN")
        print("3. Update Bank")
        print("4. Update Balance")

        choice = input("Enter Choice: ")

        if choice == "1":
            user["name"] = input("Enter New Name: ")

        elif choice == "2":
            pin = input("Enter New 4 Digit PIN: ")

            if not pin.isdigit() or len(pin) != 4:
                print("Invalid PIN!")
                return

            user["pin"] = int(pin)

        elif choice == "3":
            self.view_banks()
            bank = int(input("Enter New Bank ID: "))

            if bank not in self.banks:
                print("Invalid Bank!")
                return

            user["bank"] = bank

        elif choice == "4":
            balance = float(input("Enter New Balance: "))

            if balance < 0:
                print("Invalid Balance!")
                return

            user["balance"] = balance

        else:
            print("Invalid Choice!")
            return

        print("User Updated!")

    def delete_user(self):
        card = int(input("Enter Card Number: "))

        if card in self.users:
            del self.users[card]
            del self.history[card]
            print("User Deleted!")
        else:
            print("User Not Found!")


    def add_atm(self):
        if not self.banks:
            print("Add a bank first!")
            return

        self.view_banks()
        bank = int(input("Select Bank ID: "))

        if bank not in self.banks:
            print("Invalid Bank!")
            return

        balance = float(input("Enter Initial ATM Cash: "))

        if balance < 0:
            print("Invalid Amount!")
            return

        atm_id = max(self.atms.keys(), default=0) + 1

        self.atms[atm_id] = {
            "bank": bank,
            "balance": balance
        }

        print("ATM Created! ATM ID:", atm_id)

    def view_atms(self):
        for atm_id, atm in self.atms.items():
            print(
                "ATM ID:", atm_id,
                "| Bank:", self.banks[atm["bank"]],
                # "| Cash:", atm["balance"]
            )

    def update_atm(self):
        self.view_atms()
        atm_id = int(input("Enter ATM ID: "))

        if atm_id not in self.atms:
            print("ATM Not Found!")
            return

        print("1. Update Bank")
        print("2. Update ATM Cash")

        choice = input("Enter Choice: ")

        if choice == "1":
            self.view_banks()
            bank = int(input("Enter New Bank ID: "))

            if bank not in self.banks:
                print("Invalid Bank!")
                return

            self.atms[atm_id]["bank"] = bank

        elif choice == "2":
            balance = float(input("Enter New Cash Balance: "))

            if balance < 0:
                print("Invalid Balance!")
                return

            self.atms[atm_id]["balance"] = balance

        else:
            print("Invalid Choice!")
            return

        print("ATM Updated!")

    def delete_atm(self):
        atm_id = int(input("Enter ATM ID: "))

        if atm_id in self.atms:
            del self.atms[atm_id]
            print("ATM Deleted!")
        else:
            print("ATM Not Found!")

    def add_atm_cash(self):
        atm_id = int(input("Enter ATM ID: "))

        if atm_id not in self.atms:
            print("ATM Not Found!")
            return

        amount = float(input("Enter Cash Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        self.atms[atm_id]["balance"] += amount
        print("ATM Cash Added!")


    def add_history(self, card, message):
        self.history[card].append(message)

    def view_history(self, card):
        if not self.history[card]:
            print("No Transactions Yet!")
            return

        for transaction in self.history[card]:
            print(transaction)

    
    def login(self):

        if not self.atms:
            print("No ATM Available!")
            return

        self.view_atms()
        atm_id = int(input("Select ATM ID: "))

        if atm_id not in self.atms:
            print("Invalid ATM!")
            return

        card = int(input("Enter Card Number: "))
        pin = int(input("Enter PIN: "))

        if card not in self.users:
            print("Invalid Card Number!")
            return

        user = self.users[card]

        if user["pin"] != pin:
            print("Incorrect PIN!")
            return

        print("\nWelcome", user["name"])

        self.atm_menu(card, atm_id)

    def atm_menu(self, card, atm_id):

        while True:
            print("""
            ===== ATM MENU =====

            1. Withdraw Money
            2. Deposit Money
            3. Check Balance
            4. Account Information
            5. Transaction History
            6. Exit
            """)

            choice = input("Enter Choice: ")

            if choice == "1":
                self.withdraw(card, atm_id)

            elif choice == "2":
                self.deposit(card, atm_id)

            elif choice == "3":
                print("Balance:", self.users[card]["balance"])

            elif choice == "4":
                print("Name:", self.users[card]["name"])
                print("Card:", card)
                print("Bank:", self.banks[self.users[card]["bank"]])
                print("Balance:", self.users[card]["balance"])

            elif choice == "5":
                self.view_history(card)

            elif choice == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")


    def withdraw(self, card, atm_id):

        user = self.users[card]
        atm = self.atms[atm_id]

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        if amount > self.single_limit:
            print("Single Transaction Limit Exceeded!")
            return

        if user["withdrawn"] + amount > self.session_limit:
            print("Session Withdrawal Limit Exceeded!")
            return

        if user["count"] >= self.transaction_limit:
            print("Transaction Limit Reached!")
            return

        fee = 0

        if user["bank"] != atm["bank"]:
            fee = amount * 0.05

        total = amount + fee

        if user["balance"] < total:
            print("Insufficient Account Balance!")
            return

        if atm["balance"] < amount:
            print("Insufficient ATM Cash!")
            return

        user["balance"] -= total
        atm["balance"] -= amount

        user["withdrawn"] += amount
        user["count"] += 1

        print("Withdrawal Successful!")
        print("Withdrawal:", amount)
        print("Bank Charges:", fee)
        print("Total Deducted:", total)
        print("Remaining Balance:", user["balance"])

        self.add_history(
            card,
            f"Withdrawn: {amount}, Charges: {fee}, Total: {total}"
        )


    def deposit(self, card, atm_id):

        user = self.users[card]
        atm = self.atms[atm_id]

        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        if user["count"] >= self.transaction_limit:
            print("Transaction Limit Reached!")
            return

        user["balance"] += amount
        atm["balance"] += amount
        user["count"] += 1

        print("Deposit Successful!")
        print("New Balance:", user["balance"])

        self.add_history(card, f"Deposited: {amount}")


    def update_limits(self):
        print("Current Single Limit:", self.single_limit)
        print("Current Session Limit:", self.session_limit)
        print("Current Transaction Limit:", self.transaction_limit)

        single = float(input("Enter New Single Limit: "))
        session = float(input("Enter New Session Limit: "))
        count = int(input("Enter New Transaction Limit: "))

        if single <= 0 or session <= 0 or count <= 0:
            print("Invalid Limits!")
            return

        if session < single:
            print("Session Limit Cannot Be Less Than Single Limit!")
            return

        self.single_limit = single
        self.session_limit = session
        self.transaction_limit = count

        print("Limits Updated!")


    def admin_menu(self):

        while True:
            print("""
            ===== ADMIN PANEL =====

            1. Add Bank
            2. View Banks
            3. Update Bank
            4. Delete Bank

            5. Add User
            6. View Users
            7. Update User
            8. Delete User

            9. Add ATM
            10. View ATMs
            11. Update ATM
            12. Delete ATM
            13. Add Cash To ATM

            14. Update Transaction Limits
            15. Back
            """)

            choice = input("Enter Choice: ")

            actions = {
                "1": self.add_bank,
                "2": self.view_banks,
                "3": self.update_bank,
                "4": self.delete_bank,
                "5": self.add_user,
                "6": self.view_users,
                "7": self.update_user,
                "8": self.delete_user,
                "9": self.add_atm,
                "10": self.view_atms,
                "11": self.update_atm,
                "12": self.delete_atm,
                "13": self.add_atm_cash,
                "14": self.update_limits
            }

            if choice == "15":
                break

            action = actions.get(choice)

            if action:
                action()
            else:
                print("Invalid Choice!")


    def run(self):

        while True:
            print("""
            ===== ATM MANAGEMENT SYSTEM =====

            1. Admin Panel
            2. ATM Operations
            3. Exit
            """)

            choice = input("Enter Choice: ")

            if choice == "1":
                self.admin_menu()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

atm = ATMSystem()
atm.run()