from monsters.monster import Monster
from soldier.soldier_states.cursed_state import CursedState


class Daemon(Monster):
    def __init__(self):
        super().__init__(hp=70)

    def attack(self, soldier):
        soldier.take_damage(40)
        print("The daemon takes 40 HP from the soldier!")

    def special_attack(self, soldier):
        soldier.set_state(CursedState()) 
        print("The daemon has cursed the soldier!")