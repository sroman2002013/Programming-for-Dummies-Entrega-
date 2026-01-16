from monsters.monster import Monster
from soldier.soldier_states.scared_state import ScaredState 


class Ghost(Monster):
    def __init__(self):
        super().__init__(hp=120)

    def attack(self, soldier):
        soldier.take_damage(30)
        print("The ghost takes 30 HP from the soldier!")

    def special_attack(self, soldier):
        soldier.set_state(ScaredState())
        print("The ghost has scared the soldier!") 