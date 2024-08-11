class IFlyBehavior:
    def fly(self):
        pass
class IQuackBehavior:
    def quack(self):
        pass
    
class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("I'm flying!")
        
class FlyNoWay(IFlyBehavior):
    def fly(self):
        print("I can't fly")
        
class Quack(IQuackBehavior):
    def quack(self):
        print("Quack")
        
class Squeak(IQuackBehavior):
    def quack(self):
        print("Squeak")
        
class Duck:
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior
        
    def perform_fly(self):
        self.fly_behavior.fly()
        
    def perform_quack(self):
        self.quack_behavior.quack()
        
    def swim(self):
        print("All ducks float, even decoys!")
        
class MallardDuck(Duck):
        
    def display(self):
        print("I'm a real Mallard duck")
        
class RubberDuck(Duck):
    def display(self):
        print("I'm a rubber duck")
        
mallard = MallardDuck(FlyWithWings(), Quack())
mallard.display()
mallard.perform_fly()
mallard.perform_quack()

rubber = RubberDuck(FlyNoWay(), Squeak())
rubber.display()
rubber.perform_fly()
rubber.perform_quack()