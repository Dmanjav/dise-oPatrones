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
    
class Observable(IObservable):
    def __init__(self) -> None:
        self.observers = set()
    
    def suscribe(self, observer) -> None:
        self.observers.add(observer)
    
    def unsibscribe(self, observer) -> None:
        self.observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)
            
class IObserver(ABC):
    @abstractmethod
    def notify(self) -> None:
        pass
    
class Observer(IObserver):
    def __init__(self, observable) -> None:
        observable.suscribe(self)
    
    def notify(self, *args, **kwargs) -> None:
        print("Cambio de estado: ", args, kwargs)
        
youtuber = Observable()
suscriptor1 = Observer(youtuber)
suscriptor2 = Observer(youtuber)
youtuber.notify("Nuevo video", 1, 2, 3, descripcion="Nuevo video de Python")