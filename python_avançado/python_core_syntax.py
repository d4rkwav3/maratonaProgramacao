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
'''

class TimeInterval:

    def __init__(self, hour: int, minute: int, second: int) -> None:
        if type(hour) != int or type(minute) != int or type(second) != int:
            error_msg: str = "Use only integer numbers on object initialization"
            raise TypeError(error_msg)

        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_total_seconds(self) -> int:
        return (self.__hour * 3600) + (self.__minute * 60) + self.__second

    def get_hour(self) -> int:
        return self.__hour

    def get_minute(self) -> int:
        return self.__minute

    def get_second(self) -> int:
        return self.__second

    def __str__(self) -> str:
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    def __add__(self, time):
        if type(time) != TimeInterval:
            error_msg: str = "Type Error, use TimeInterval objects only!"
            raise TypeError(error_msg)
        
        hour, min, sec = time.get_hour(), time.get_minute(), time.get_second()
        total_sec = (hour * 3600) + (min * 60) + sec

        total_time = self.get_total_seconds() + total_sec

        result_sec = ((total_time / 60) - (total_time // 60)) * 60
        min1 = (total_time // 60)
        result_min = ((min1 / 60) - (min1 // 60)) * 60
        result_hour = total_time // 3600

        time_result = "{:d}:{:.0f}:{:.0f}".format(result_hour if result_hour >= 10 else str(result_hour).zfill(1), result_min, result_sec)

        return time_result

    def __sub__(self, time):
        if type(time) != TimeInterval:
            error_msg: str = "Type Error, use TimeInterval objects only!"
            raise TypeError(error_msg)
        
        hour, min, sec = time.get_hour(), time.get_minute(), time.get_second()
        total_sec = (hour * 3600) + (min * 60) + sec

        total_time = self.get_total_seconds() + (-total_sec)

        result_sec = ((total_time / 60) - (total_time // 60)) * 60
        min1 = (total_time // 60)
        result_min = ((min1 / 60) - (min1 // 60)) * 60
        result_hour = total_time // 3600

        time_result = "{:d}:{:.0f}:{:.0f}".format(result_hour if result_hour >= 10 else str(result_hour).zfill(1), result_min, result_sec)

        return time_result

    def __mul__(self, number: int):
        if type(number) != int:
            error_msg: str = "TimeInterval can only be multiplied with integers"
            raise TypeError(error_msg)

        hour, min, sec = self.get_hour(), self.get_minute(), self.get_second()
        total_sec = (hour * 3600) + (min * 60) + sec

        total_time = self.get_total_seconds() * number

        result_sec = ((total_time / 60) - (total_time // 60)) * 60
        min1 = (total_time // 60)
        result_min = ((min1 / 60) - (min1 // 60)) * 60
        result_hour = total_time // 3600

        time_result = "{:d}:{:.0f}:{:.0f}".format(result_hour if result_hour >= 10 else str(result_hour).zfill(1), result_min, result_sec)

        return time_result        

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * 2)
#error_testing = TimeInterval(0, 0, '0') #Ok!
# TODO: Muito código sendo repetido, vou pensar em como fazer uma ou mais funções pra reduzir isso