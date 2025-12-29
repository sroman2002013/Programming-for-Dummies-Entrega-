from monster import Monster
from soldier.soldier_states.troll_state import TrollState

class Troll(Monster):
    def __init__(self):
        super().__init__(hp=90)

    def attack(self, soldier):
        damage = 30
        if self.hp <= 50:
            damage += 2
        soldier.take_damage(damage)


    def special(self, soldier):
        soldier.set_state(TrollState()) # TODO: States??? 