from soldier_state import SoldierState
import random

class ScaredState(SoldierState):
    def can_act(self) -> bool:
        allowed = random.choice([True, False])
        if not allowed:
            # TODO: print i'm scared ???
            print("I'm scared....")
        return allowed