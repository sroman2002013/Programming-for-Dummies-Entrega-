from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, hp: int):
        self.hp = hp

    def take_damage(self, damage: int):
        self.hp -= damage
        
        
    @abstractmethod
    def attack(self, soldier):
        pass

    @abstractmethod
    def special_attack(self, soldier):
        pass