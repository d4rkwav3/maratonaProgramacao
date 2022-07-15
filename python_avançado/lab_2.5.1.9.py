'''
Objectives

    improving the student's skills in operating with static and class methods

Scenario

    Create a class representing a luxury watch;
    The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
    the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
    the regular __init__ method should only increase the value of the appropriate class variable;

The text intended to be engraved should follow some restrictions:

    it should not be longer than 40 characters;
    it should consist of alphanumerical characters, so no space characters are allowed;
    if the text does not comply with restrictions, an exception should be raised;

before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

    Create a watch with no engraving
    Create a watch with correct text for engraving
    Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
    After each watch is created, call class method to see if the counter variable was increased
'''

class ExpensiveWatch:
    __watches_created = 0

    def __init__(self) -> None:
        ExpensiveWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return f'Number of Luxury Watches created: {cls.__watches_created}'

    @classmethod
    def add_engraving(cls, text: str):
        if cls.validate_engraving(text):
            _watch = cls()
            _watch._engraved_text = text
            return _watch
        else:
            raise ValueError('Invalid Text Format, use ExpensiveWatch.validate_engraving() for more information.')

    @staticmethod
    def validate_engraving(text: str) -> bool:
        if type(text) is not str:
            return False

        elif len(text) > 40:
            raise ValueError('Engraving text too long! Max lenght is 40 characters.')
        
        else:
            special_chars = 0
            for ch in text:
                if ch.isalnum():
                    continue
                else:
                    special_chars += 1

            if special_chars > 0:
                raise ValueError('Special characters not allowed! Use alphanumerical characters only.')
            else:
                return True

watch1 = ExpensiveWatch()
watch2 = ExpensiveWatch.add_engraving("PythonIsEasyToLearn")

try:
    watch3 = ExpensiveWatch.add_engraving("Python is cool but so is Java!")
except ValueError:
    pass

print(ExpensiveWatch.get_number_of_watches_created())