from weapon import Weapon

class Gun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=10)

    def shoot(self, target, damage_multiplier):
        if self._consume(1):
            target.take_damage(30, damage_multiplier)

    def reload(self):
        self.ammunition = self.max_ammunition