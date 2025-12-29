from soldier_state import SoldierState
from soldier import Soldier

class CursedState(SoldierState):
    
    def on_turn_start(self, soldier):
        soldier.take_damage(50)
        # TODO: print???
