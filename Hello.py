class Student:
    __name = None

    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name

hello = Student()

hello.setName(input())

print("Hello,", hello.getName(), end='')