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
        self.size: int = size
        self.pressure: float = 0

    def get_pressure(self) -> None:
        if self.pressure >= 12:
            print("Pressure is good!")
        else:
            print("Not looking good! Check your tires before use!")

    def pump(self, pressure) -> None:
       self.pressure = pressure 

class Engine:
    def __init__(self, fuel_type) -> None:
        self.fuel: str = fuel_type
        self.engine_on: bool = False

    def start(self):
        self.engine_on = True

    def stop(self):
        self.engine_on = False

    def get_state(self):
        if self.engine_on:
            print("The engine is on.")
        else:
            print("The engine is off.")

class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN: str = VIN #vehicle identification number
        self.engine = engine
        self.tires = tires

#tires
city_tires = Tires(15)
offroad_tires = Tires(18)
#engines
electric_engine = Engine("Electric")
petrol_engine = Engine("Combustion")
#cars
city_car = Vehicle("PY256CT", electric_engine, city_tires)
off_track = Vehicle("PY512OR", petrol_engine, offroad_tires)

city_car.tires.pump(10)
off_track.tires.pump(13)
city_car.tires.get_pressure()
off_track.tires.get_pressure()

city_car.engine.start()
off_track.engine.stop()
city_car.engine.get_state()
off_track.engine.get_state()