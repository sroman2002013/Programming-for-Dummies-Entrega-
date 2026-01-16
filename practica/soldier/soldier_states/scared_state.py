from soldier.soldier_states.soldier_state import SoldierState
import random

class ScaredState(SoldierState):
    def can_act(self) -> bool:
        allowed = random.choice([True, False])
        if not allowed:
            print("Scared, cant attack")
        return allowed