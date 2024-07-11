# Private members are exclusively accessible within the class. 
# To mark a member as private, prefix its name with double underscores (__).


class BankAccount:

    def __init__(self, account_number):
        self.__account_number = account_number  # Private attribute
    
    def __validate_pin(self, pin):
        return len(str(pin)) == 4


# Creating an instance of the class
account = BankAccount("12345")


# Accessing private attributes using name mangling
print(account._BankAccount__account_number)  # Output: 12345


# Accessing private method using name mangling
print(account._BankAccount__validate_pin(1234))  