# Mehrzad Nahavandi
# A01231818

import re

class BankAccount:
    """class bank account with two input name and balance"""
    def __init__(self, name, balance):


        # name cannot be empty
        if re.search("^(\s*)$",name):
            raise ValueError("name cannot be empty")


        # name cannot be any numbers or symbols
        pattern = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(bool(re.search(r'\d', name))) or re.search(pattern,name):
            raise ValueError("name cannot include numbers or symbols")


        #balance
        if balance < 0 :
            raise ValueError("balance cannot be negative number")
        else:
            self.name = name.title()
            self.balance = balance



    def displayDetails(self):
        """displays name and balance"""
        print("name is: %s"%self.name)
        print("balance is: %0.1f"%self.balance)



    def deposit(self, amount):
        """perform deposit"""
        if amount > 0 :
            self.balance += amount
            return self.balance
        else :
            raise ValueError("amount cannot be zero or less")



    def withdraw(self, amount):
        """perform withdraw"""
        if amount <= 0 :
            raise ValueError("amount cannot be zero or less than zero")

        elif amount > self.balance :
            raise ValueError("Insufficient funds")

        else:
            self.balance -= amount
            return self.balance
