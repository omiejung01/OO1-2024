from datetime import datetime

class Account:
    def __init__(self,account_name, opening_balance):
        self.__account_name = account_name
        self.__balance = opening_balance
        self.__created_date = datetime.now()
        self.__activated = True

    def display(self):
        status = 'Deactivated'
        if self.__activated:
            status = 'Activated'
        return self.__account_name + ' - since ' + self.__created_date.strftime("%b %d, %Y") + ' - status: ' + status

    def balanceInquiry(self):
        return f"{self.__balance:,.2f}"

class CreditCard(Account):
    def __init__(self, credit, account_name, opening_balance):
        self.__credit = credit
        self.__due_date = None
        self.__extended_limit = 0
        self.__extended_until_date = None
        super().__init__(account_name, opening_balance)

    def display(self):
        return super().display() + ' credit: ' + f"{self.__credit:,.2f}"        # print(super().__account_name + ' has an account balance: ' + str(super().__balance))

    def display_extended(self):
        print('This is for extended account')

def my_sum(args):
    # input can be string, list of int, or dictionary of int
    # Polymorphism #2 (data type)
    sum = 0
    if type(args) == str:
        numbers = args.split()
        for n in numbers:
            sum += int(n)

    if type(args) == list:
        for n in args:
            sum += n

    if type(args) == dict:
        vals = args.values()
        for n in vals:
            sum += n

    return sum

if __name__ == '__main__':
    accountC = Account("Mr. C", 5000)
    print(accountC.display())
    print(accountC.balanceInquiry())

    creditcardD = CreditCard(10000, "Mr. D", 0)
    print(creditcardD.display())

    #print('A' + 'B' + 'C')
    #print(1 + 2 + 3)

    #print(len('Hello'))
    mylist = [1, 2, 3, 'gg']
    #print(len(mylist))

    mystr = "1 2 3 4"
    print(my_sum(mystr))

    mylist2 = [ 1 , 2 , 3 ,4 , 5]
    print(my_sum(mylist2))

    mydict = {
        "a": 10,
        "b": 20,
        "c": 30
    }
    print(my_sum(mydict))





