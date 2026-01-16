from monsters.monster import Monster

class MonsterTeam:

    def __init__(self, monsters=[]):
        self.monsters = monsters

    def add(self, monster: Monster):
        self.monsters.append(monster)

    def remove_dead(self):
        self.monsters = [m for m in self.monsters if m.is_alive()]

    def all_dead(self) -> bool:
        self.remove_dead()
        return len(self.monsters) == 0
    
    
    