# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기화
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    # 입금
    def deposit(self, amount):
        self.__balance += amount 
    # 출금
    def withdraw(self, amount):
        self.__balance -= amount
    # def setBalance(self, balance):
    #     self.__balance = balance
    # 결과 .toString()
    def __str__(self):
        # from Object class
        return "{0} , {1} , {2}".format(self.__id, self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(200, "전우치", 15000)
account1.withdraw(3000)
print(account1)

# account1.__balance = 12345
# print(account1.__balance)
# account1.setBalance(99999)
# print(account1)