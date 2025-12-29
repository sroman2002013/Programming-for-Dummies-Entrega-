from monster import Monster
from soldier.soldier_states.scared_state import ScaredState 


class Ghost(Monster):
    def __init__(self):
        super().__init__(hp=130)

    def attack(self, soldier):
        soldier.take_damage(30)

    def special(self, soldier):
        soldier.set_state(ScaredState()) 