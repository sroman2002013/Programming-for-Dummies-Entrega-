from weapons.weapon import Weapon

class Gun(Weapon):
    def __init__(self):
        super().__init__(max_ammunition=10)

    def shoot(self, target, damage_multiplier = 1):
        if self._consume(1):
            target.take_damage(30, damage_multiplier)
            print(f"Gun deals {30 * damage_multiplier} damage!")

    def reload(self):
        self.ammunition = self.max_ammunition
        print("Gun reloaded to maximum ammunition.")