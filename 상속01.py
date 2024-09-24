class Person:
    def __init__(self, name, phoneNumber):
        self.__name = name
        self.__phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.__name, self.__phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        super().__init__(name, phoneNumber)
        self.__subject = subject
        self.__studentID = studentID

    def printInfo(self):
        # print("\nInfo(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        super().printInfo()
        print("Info(Subject:{0}, Student ID: {1})".format(self.__subject, self.__studentID))

# 인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
print()
s.printInfo()
# print(p.__dict__)
# print(s.__dict__)


