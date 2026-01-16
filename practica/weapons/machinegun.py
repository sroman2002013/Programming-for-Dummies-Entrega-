from weapons.weapon import Weapon
import random

class Machinegun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=15)

    def shoot(self, target, damage_multiplier = 1):
        if self._consume(3):
            total_damage = 0
            for _ in range(3):
                if random.choice([True, False]): 
                    total_damage += 30
            target.take_damage(total_damage * damage_multiplier)
            print(f"Machinegun deals {total_damage * damage_multiplier} damage!")
    def reload(self):
        self.ammunition = self.max_ammunition
        print("Machinegun reloaded to maximum ammunition.")