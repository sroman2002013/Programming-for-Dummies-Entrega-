from weapon import Weapon
import random

class Machinegun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=15)

    def shoot(self, target, damage_multiplier):
        if self._consume(3):
            hits = random.randint(1, 3)
            target.take_damage(hits * 30 * damage_multiplier)

    def reload(self):
        self.ammunition = self.max_ammunition