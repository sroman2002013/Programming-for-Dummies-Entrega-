from abc import ABC, abstractmethod
import random

class Weapon(ABC):
    def __init__(self, max_ammunition):
        self.max_ammunition = max_ammunition
        self.ammunition = max_ammunition

    def _consume(self, n) -> bool:
        if self.ammunition < n:
            print("No ammunition")
            return False
        self.ammunition -= n
        return True

    @abstractmethod
    def shoot(self, target, damage_multiplier = 1):
        pass

    @abstractmethod
    def reload(self):
        pass