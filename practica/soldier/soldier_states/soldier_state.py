from abc import ABC, abstractmethod

class SoldierState(ABC):

    def on_turn_start(self, soldier):
        pass

    def can_act(self) -> bool:
        return True