# Mehrzad Nahavandi
# A01231818

import BankAccount as Bank


def main():
    """check validation of entries then perform action required """
    while True:
        try:
            print("creating a bank account")
            name = input("enter the account holder name: ")
            balance = int(input("enter the balance: "))
            bank_account = Bank.BankAccount(name,balance)
            bank_account.displayDetails()


            while True:
                try:
                    print("1 _ deposit")
                    print("2 _ withdraw")
                    choice = input("enter your choice: ")
                    if choice == "1":
                        print(" your choice is 1 ")
                        amount = int(input("enter the amount to deposit: "))
                        balance = bank_account.deposit(amount)
                        bank_account = Bank.BankAccount(name, balance)
                        bank_account.displayDetails()

                    elif choice == "2":
                        print(" your choice is 2 ")
                        amount = int(input("enter the amount to withdraw: "))
                        balance = bank_account.withdraw(amount)
                        bank_account = Bank.BankAccount(name, balance)
                        bank_account.displayDetails()

                    else:
                        print(" invalid choice ")

                except ValueError as v:
                    print(v)
                input_reply = input("do you want to make another transaction?yes/no:")
                if input_reply.lower() == "yes":
                    continue
                else:
                    return
        except ValueError as v:
            print(v)
            print("try again")





if __name__ == "__main__":
    main()