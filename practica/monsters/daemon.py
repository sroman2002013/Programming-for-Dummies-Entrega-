from monster import Monster
from soldier.soldier_states.cursed_state import CursedState


class Daemon(Monster):
    def __init__(self):
        super().__init__(hp=90)

    def attack(self, soldier):
        soldier.take_damage(40)

    def special(self, soldier):
        soldier.set_state(CursedState()) 