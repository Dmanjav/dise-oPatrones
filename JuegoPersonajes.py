class IAttackBehavior:
    def attack(self):
        pass
    
class IDefenseBehavior:
    def defense(self):
        pass
    
class SwordAttack(IAttackBehavior):
    def attack(self):
        print("Ataque con espada")
        
class BowAttack(IAttackBehavior):
    def attack(self):
        print("Ataque con arco")

class MagicAttack(IAttackBehavior):
    def attack(self):
        print("Ataque con magia")
        
class ShieldDefense(IDefenseBehavior):
    def defense(self):
        print("Defensa con escudo")
        
class DodgeDefense(IDefenseBehavior):
    def defense(self):
        print("Defensa con esquive")
        
class MagicDefense(IDefenseBehavior):
    def defense(self):
        print("Defensa con magia")
        
class Character:
    def __init__(self, name, vida, attack_behavior, defense_behavior, attack, defense):
        self.name = name
        self.vida = vida
        self.attack_behavior = attack_behavior
        self.defense_behavior = defense_behavior
        self.attack = attack
        self.defense = defense
        
    def is_alive(self):
        return self.vida > 0
    
    def perform_attack(self, enemy):
        print(f"{self.name} ataca a {enemy.name}")
        print(f"{enemy.name} tiene {enemy.vida} puntos de vida")
        if enemy.is_alive():
            self.attack_behavior.attack()
            if enemy.defense > 0:
                enemy.perform_defense()
            enemy.receive_damage(self.attack)
        
    def perform_defense(self):
        self.defense_behavior.defense()
        self.defense -= 2
        
        
    def receive_damage(self, damage):
        self.vida -= damage
        if self.vida <= 0:
            print(f"{self.name} ha muerto")
        else:
            print(f"Los puntos de vida de {self.name} son {self.vida}")    
        
    def display(self):
        print(f"El personaje se llama {self.name}")
        print(f"{self.name} tiene {self.vida} puntos de vida")
        print(f"{self.name} tiene {self.attack} puntos de ataque")
        print(f"{self.name} tiene {self.defense} puntos de defensa")
    
    
class Archer(Character):
    def __init__(self, name, vida, attack_behavior, defense_behavior, attack, defense, arrows):
        super().__init__(name, vida, attack_behavior, defense_behavior, attack, defense)
        self.arrows = arrows
        
    def display(self):
        super().display()
        print(f"{self.name} tiene {self.arrows} flechas")
        
    def perform_attack(self, enemy):
        super().perform_attack(enemy)
        self.arrows -= 1
        
class Warrior(Character):
    def __init__(self, name, vida, attack_behavior, defense_behavior, attack, defense, sword):
        super().__init__(name, vida, attack_behavior, defense_behavior, attack, defense)
        self.sword = sword
        
    def display(self):
        super().display()
        print(f"{self.name} tiene {self.sword} espada")
        
    def perform_attack(self, enemy):
        super().perform_attack(enemy)
        self.sword -= 1
        
class Mage(Character):
    def __init__(self, name, vida, attack_behavior, defense_behavior, attack, defense, magic):
        super().__init__(name, vida, attack_behavior, defense_behavior, attack, defense)
        self.magic = magic
        
    def display(self):
        super().display()
        print(f"{self.name} tiene {self.magic} magia")
        
    def perform_attack(self, enemy):
        super().perform_attack(enemy)
        self.magic -= 1
        
def combat(p1, p2):
    while p1.is_alive() and p2.is_alive():
        p1.perform_attack(p2)
        p2.perform_attack(p1)
        
    if p1.is_alive():
        print(f"{p1.name} ha ganado")
    else:
        print(f"{p2.name} ha ganado")
        
p1 = Character("Gandalf", 100, MagicAttack(), ShieldDefense(), 30, 10)
p2 = Character("Sauron", 100, SwordAttack(), ShieldDefense(), 20, 10)
a = Archer("Legolas", 100, BowAttack(), DodgeDefense(), 50, 5, 10)
w = Warrior("Aragorn", 100, SwordAttack(), ShieldDefense(), 40, 10, 1)
m = Mage("Gandalf", 100, MagicAttack(), MagicDefense(), 30, 5, 5)

combat(p1, p2)
print("*" * 15)
combat(a, w)
print("*" * 15)
combat(m, w)
