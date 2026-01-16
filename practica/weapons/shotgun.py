from weapons.weapon import Weapon

class Shotgun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=3)

    def shoot(self, target, damage_multiplier = 1):
        if self._consume(1):
            target.take_damage(60 * damage_multiplier)
            print(f"Shotgun deals {60 * damage_multiplier} damage!")

    def reload(self):
        self.ammunition = min(self.ammunition + 1, self.max_ammunition)
        print("Shotgun reloaded by 1 round.")