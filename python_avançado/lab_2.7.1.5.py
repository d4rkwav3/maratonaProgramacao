'''
Objectives

    improving the student's skills in operating with the getter, setter, and deleter methods;
    improving the student's skills in creating their own exceptions.

Scenario

    Implement a class representing an account exception,
    Implement a class representing a single bank account,
    This class should control access to the account number and account balance attributes by implementing the properties:
        it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
        it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
        when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
        it should not be possible to delete an account as long as the balance is not zero;
    test your class behavior by:
        setting the balance to 1000;
        trying to set the balance to -200;
        trying to set a new value for the account number;
        trying to deposit 1.000.000;
        trying to delete the account attribute containing a non-zero balance.

'''
class AccountException(AttributeError):
    pass

class BankAccount:
    def __init__(self, accountnumber, initialbalance=0) -> None:
        self.__bank_id: int = accountnumber
        self.__balance: float = initialbalance

    @property
    def bank_id(self):
        return self.__bank_id

    @property
    def balance(self):
        return self.__balance

    @bank_id.setter
    def bank_id(self, number: int):
        alarm = "Illegal action detected! Cannot change account number!!"
        raise AccountException(alarm)

    @balance.setter
    def balance(self, amount: float):
        if amount >= 100000:
            print("\nSuspect activity detected! Fraud Agency notified.")
            self.__balance = amount
            print(f"\tYour current balance is R$ {amount:.2f}")
        elif amount > 0 and amount < 100000:
            self.__balance = amount
            print(f"Your current balance is R$ {amount:.2f}")
        elif amount < 0:
            error = "insufficient balance to make this operation!"
            raise AccountException(error)

    @bank_id.deleter
    def bank_id(self):
        ac_num = self.__bank_id
        if self.__balance > 0:
            error = "Account balance not empty! Please withdraw all remaining values before account exclusion"
            raise AccountException(error)
        else:
            self.__bank_id = None
            print(f"Bank Account number {ac_num} is now permanently closed.")

make_me_happy = BankAccount(123456, 0)

print(f"You account is now avalible to use >> {make_me_happy.bank_id} is your account number")
print(f"Your current balance is R$ {make_me_happy.balance:.2f}")

make_me_happy.balance = 1000

try:
    make_me_happy.balance = -200
except AccountException as ac:
    print("\nTrying to deposit a negative number to account:\n\tResult: ", ac)

try:
    make_me_happy.bank_id = 654321
except AccountException as ac:
    print("\nTrying to change account number:\n\tResult: ", ac)

make_me_happy.balance = 1000000

try:
    del make_me_happy.bank_id
except AccountException as ac:
    print("\nTrying to delete the bank_id attribute:\n\tResult: ", ac)