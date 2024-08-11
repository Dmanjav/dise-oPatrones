from abc import ABC, abstractmethod

class CarBuilder(ABC):
    @abstractmethod
    def set_wheels(self, Num: int) -> None:
        pass

    @abstractmethod
    def set_color(self, Color: str) -> None:
        pass

    @abstractmethod
    def set_gps(self, value: bool) -> None:
        pass

    @abstractmethod
    def get_result(self) -> 'Car':
        pass

class CarManualBuilder(ABC):
    @abstractmethod
    def set_wheels(self, Num: int) -> None:
        pass

    @abstractmethod
    def set_color(self, Color: str) -> None:
        pass

    @abstractmethod
    def set_gps(self, value: bool) -> None:
        pass

    @abstractmethod
    def get_result(self) -> 'Manual':
        pass
    
class SedanCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, Num: int):
        self.car.wheels = Num
        return self

    def set_color(self, Color: str):
        self.car.color = Color
        return self

    def set_gps(self, value: bool):
        self.car.gps = value
        return self

    def get_result(self):
        return self.car
    
class SedanCarManualBuilder(CarManualBuilder):
    def __init__(self):
        self.manual = Manual()

    def set_wheels(self, Num: int):
        self.manual.wheels = Num
        return self

    def set_color(self, Color: str):
        self.manual.color = Color
        return self

    def set_gps(self, value: bool):
        self.manual.gps = value
        return self

    def get_result(self):
        return self.manual
    
class Manual:
    def __init__(self):
        self.wheels = None
        self.color = "None"
        self.gps = False

    def __str__(self) -> str:
        return f"Manual car with {self.wheels} wheels, color {self.color} and GPS: {self.gps}"

class Car:
    def __init__(self):
        self.wheels = None
        self.color = "None"
        self.gps = False

    def __str__(self) -> str:
        return f"Car with {self.wheels} wheels, color {self.color} and GPS: {self.gps}"
    
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_wheels(4).set_color("Red").set_gps(True)
        return self.builder.get_result()
    
sedanBuilder = SedanCarBuilder()
director = Director(sedanBuilder)
car = director.construct()

manualSedanBuilder = SedanCarManualBuilder()
director2 = Director(manualSedanBuilder)
manual = director2.construct()
print(manual)