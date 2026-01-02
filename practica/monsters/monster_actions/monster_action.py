from abc import ABC, abstractmethod

class MonsterAction(ABC):
    @abstractmethod
    def execute(self, soldier):
        pass