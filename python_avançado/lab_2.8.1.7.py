'''
Objectives

    improving the student's skills in operating with inheritance and composition

Scenario

Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

    define classes representing:
        tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
        engine; methods available: start(), stop(), get_state(); attribute available: fuel type
        vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
    based on the classes defined above, create the following objects:
        two sets of tires: city tires (size: 15), off-road tires (size: 18)
        two engines: electric engine, petrol engine
    instantiate two objects representing cars:
        the first one is a city car, built of an electric engine and city tires
        the second one is an all-terrain car build of a petrol engine and off-road tires
    play with the cars by calling methods responsible for interaction with components.

'''

class Tires:
    def __init__(self, size: int) -> None:
        self.size = size
    
    def get_pressure(self, ready):
        if type(ready) == str and ready == "pump":
            print("Pressure is good!")
        else:
            print("Not looking good! Check your tires before use!")

    def pump(self):
        print ("Tires pumped! Ready for use.")

class Engine:
    def __init__(self, fuel, type) -> None:
        self.fuel = fuel
        self.type = type

# pneu = Tires(15)
# print(type(pneu.pump))
# print(pneu.pump.__name__)
# pneu.get_pressure(pneu.pump.__name__)