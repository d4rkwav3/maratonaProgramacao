'''
Objectives

    improving the student's skills in operating with metaclasses;
    improving the student's skills in operating with class variables and class methods.

Scenario

    Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
    the system was created by a group of volunteers who worked with no clear “clean coding” rules;
    the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
    your task is to prepare a metaclass that is responsible for:
        equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
        equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.

* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

    Your metaclass should be used to create a few distinct legacy classes;
    create objects based on the classes;
    list the class names that are instantiated by your metaclass.

'''
from datetime import datetime as dt

def get_instantiation_time(self):
    return self.instantiation_time

class CodeCleanUp(type):
    instantiated_classes = []

    def __new__(mcs, name, bases, dictionary):
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = dt.now().strftime("%H:%M:%S of %d-%m-%y")
        CodeCleanUp.instantiated_classes.append(obj.__name__)
        return obj

class Greeting(metaclass=CodeCleanUp):
    def greeting(self, name):
        return "Hello {}!".format(name if type(name) == str else 'User')

class Person(metaclass=CodeCleanUp):
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    def get_name(self):
        return self.__name

    def get_person_data(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nGender: {self.__gender}"

me = Person("Bruno", 31, "Male")
hello = Greeting()
print(me.get_person_data())
print()
print(hello.greeting(me.get_name()))
print()
print(CodeCleanUp.instantiated_classes)
print()
print("Person class created", me.get_instantiation_time())
print("Greetings class created", hello.get_instantiation_time())