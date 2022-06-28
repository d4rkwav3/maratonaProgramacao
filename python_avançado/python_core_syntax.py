'''
2.1.1.10 Python core syntax: LAB #1
Scenario
    Create a class representing a time interval;
    the class should implement its own method for addition, subtraction on time interval class objects;
    the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
    check the argument type, and in case of a mismatch, raise a TypeError exception.

Hint #1
    just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
    for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

    Test data:
        the first time interval (fti) is hours=21, minutes=58, seconds=50
        the second time interval (sti) is hours=1, minutes=45, seconds=22
        the expected result of addition (fti + sti) is 23:44:12
        the expected result of subtraction (fti - sti) is 20:13:28
        the expected result of multiplication (fti * 2) is 43:57:40


Hint #2
    you can use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.

2.1.1.11 Python core syntax: LAB #2
Scenario

    Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
    to add an integer to a time interval object means to add seconds;
    to subtract an integer from a time interval object means to remove seconds.


    in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.

Test data:

    the time interval (tti) is hours=21, minutes=58, seconds=50
    the expected result of addition (tti + 62) is 21:59:52
    the expected result of subtraction (tti - 62) is 21:57:48
'''

class TimeInterval:

    def __init__(self, hour: int, minute: int, second: int) -> None:
        if type(hour) != int or type(minute) != int or type(second) != int:
            error_msg: str = "Use only integer numbers on object initialization"
            raise TypeError(error_msg)

        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__only_seconds = (self.__hour * 3600 if self.__hour > 0 else 0) + (self.__minute * 60 if self.__minute > 0 else 0) + self.__second

    def get_total_seconds(self) -> int:
        return self.__only_seconds

    def seconds_to_hours(self, total_seconds: int) -> str:
        result_sec = ((total_seconds / 60) - (total_seconds // 60)) * 60
        min = (total_seconds // 60)
        result_min = ((min / 60) - (min // 60)) * 60
        result_hour = total_seconds // 3600
        time_result = "{:d}:{:.0f}:{:.0f}".format(result_hour, result_min, result_sec)
        return time_result

    def get_hour(self) -> int:
        return self.__hour

    def get_minute(self) -> int:
        return self.__minute

    def get_second(self) -> int:
        return self.__second

    def __str__(self) -> str:
        hours, minutes, seconds = str(self.get_hour()), str(self.get_minute()), str(self.get_second())
        return f'{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}'

    def __add__(self, time):
        if type(time) == TimeInterval:
            total_time = self.get_total_seconds() + time.get_total_seconds()
            formatted_time = self.seconds_to_hours(total_time)
            result = TimeInterval(int(formatted_time[0:2]), int(formatted_time[3:5]), int(formatted_time[6:8]))

            return result

        elif type(time) == int:
            new_time = TimeInterval(0, 0, time)
            total_time = self.get_total_seconds() + new_time.get_total_seconds()
            formatted_time = self.seconds_to_hours(total_time)
            result = TimeInterval(int(formatted_time[0:2]), int(formatted_time[3:5]), int(formatted_time[6:8]))

            return result

        else:
            error_msg: str = "Type Error, use TimeInterval objects or integer number only!"
            raise TypeError(error_msg)

    def __sub__(self, time):
        if type(time) == TimeInterval:
            total_time = self.get_total_seconds() + (-time.get_total_seconds())
            formatted_time = self.seconds_to_hours(total_time)
            result = TimeInterval(int(formatted_time[0:2]), int(formatted_time[3:5]), int(formatted_time[6:8]))

            return result

        elif type(time) == int:
            new_time = TimeInterval(0, 0, time)
            total_time = self.get_total_seconds() + (-new_time.get_total_seconds())
            formatted_time = self.seconds_to_hours(total_time)
            result = TimeInterval(int(formatted_time[0:2]), int(formatted_time[3:5]), int(formatted_time[6:8]))

            return result

        else:
            error_msg: str = "Type Error, use TimeInterval objects or integer number only!"
            raise TypeError(error_msg)

    def __mul__(self, number: int):
        if type(number) != int:
            error_msg: str = "TimeInterval can only be multiplied with integers"
            raise TypeError(error_msg)

        total_time = self.get_total_seconds() * number
        formatted_time = self.seconds_to_hours(total_time)
        result = TimeInterval(int(formatted_time[0:2]), int(formatted_time[3:5]), int(formatted_time[6:8]))

        return result       

#error_test = TimeInterval(0, 0, '0') #Ok!
fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * 2)
tti = TimeInterval(21, 58, 50)
print(tti + 62)
print(tti - 62)