from abc import ABC, abstractmethod

class IObservable(ABC): 
    @abstractmethod
    def suscribe(self, observer) -> None:
        pass
    
    @abstractmethod
    def unsibscribe(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
    
class EstacionMeteorologica(IObservable): # Estacion
    def __init__(self) -> None:
        self.observers = set()
    
    def suscribe(self, observer) -> None:
        self.observers.add(observer)
    
    def unsibscribe(self, observer) -> None:
        self.observers.remove(observer)
    
    def cambiar_clima(self, *args, **kwargs) -> None:
        self.notify(*args, **kwargs)
    
    def notify(self, *args, **kwargs) -> None:
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)
            
class IObserver(ABC):
    @abstractmethod
    def notify(self) -> None:
        pass
    
class DispositivoAlerta(IObserver):
    def __init__(self, observable, name) -> None:
        observable.suscribe(self)
        self.name = name
    
    def notify(self, observable, *args, **kwargs) -> None:
        print(f"Alerta, el dispositivo {self.name}: ", args, kwargs)
    
estacion = EstacionMeteorologica()
dispositivo1 = DispositivoAlerta(estacion, "Disp 1")
dispositivo2 = DispositivoAlerta(estacion, "Disp 2")
estacion.cambiar_clima("Lluvia", "super fuerte", resumen="Lluvia en la tarde", temperatura=25)