from abc import ABC, abstractmethod

class SoldierAction(ABC):

    @abstractmethod
    def execute(self, soldier):
        pass