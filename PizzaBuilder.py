from abc import ABC, abstractmethod

class Pizza:
    def __init__(self) -> None:
        self.size = None
        self.cheese = None
        self.ingredients = []
        
    def __str__(self) -> str:
        return f"Size: {self.size}, Cheese: {self.cheese}, Ingredients: {self.ingredients}"

class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size: str) -> None:
        self.pizza.size = size
    
    @abstractmethod
    def set_cheese(self, cheese: str) -> None:
        self.pizza.cheese = cheese
    
    @abstractmethod
    def add_ingredient(self, ingredient: list) -> None:
        self.pizza.ingredients.append(ingredient)
    
    @abstractmethod
    def get_result(self):
        self.pizza = Pizza()
        

class CustomPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size: str):
        self.pizza.size = size
        return self
    
    def set_cheese(self, cheese: str):
        self.pizza.cheese = cheese
        return self
    
    def add_ingredient(self, ingredient: list):
        self.pizza.ingredients.append(ingredient)
        return self
    
    def get_result(self):
        return self.pizza
    
class Chef:
    def __init__(self, builder: PizzaBuilder) -> None:
        self.builder = builder
    
    def cook_pizza(self, size: str, cheese: str, igredients: list):
        self.builder.set_size(size).set_cheese(cheese).add_ingredient(igredients)
        return self.builder.get_result()
    
pizza = CustomPizzaBuilder()
chef = Chef(pizza)
fin = chef.cook_pizza("Medium", "Mozzarella", ["Pepperoni", "Sausage", "Mushrooms"])
print(fin)