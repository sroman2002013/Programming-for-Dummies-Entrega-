from soldier.soldier_states.soldier_state import SoldierState
from soldier.soldier import Soldier

class CursedState(SoldierState):
    
    def on_turn_start(self, soldier):
        soldier.take_damage(50)
        print("Cursed soldier takes 50 damage at the start of turn.")