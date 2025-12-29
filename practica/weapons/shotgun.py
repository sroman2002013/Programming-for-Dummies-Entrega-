from weapon import Weapon

class Shotgun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=3)

    def shoot(self, target, damage_multiplier):
        if self._consume(1):
            target.take_damage(60 * damage_multiplier)

    def reload(self):
        self.ammunition = min(self.ammunition + 1, self.max_ammunition)