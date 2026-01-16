from monsters.monster_team import MonsterTeam
from monsters.troll import Troll
from monsters.daemon import Daemon
from monsters.ghost import Ghost

class MonsterFactory:
    
    MONSTER_MAP = {
        "1": Troll,
        "2": Ghost,
        "3": Daemon
    }

    @staticmethod
    def create_team(size: int = 3) -> MonsterTeam:
        monsters = []
        print(f"--- Building Monster Team ({size} members) ---")
        
        for i in range(1, size + 1):
            monsters.append(MonsterFactory._create_single_monster(i))
            
        return MonsterTeam(monsters)

    @staticmethod
    def _create_single_monster(index: int):
        print(f"1: Troll | 2: Ghost | 3: Daemon")
        choice = input(f"Choose monster #{index}: ")
        
        while choice not in MonsterFactory.MONSTER_MAP:
            print("Invalid option.")
            choice = input(f"Choose monster #{index}: ")
            
        monster_class = MonsterFactory.MONSTER_MAP[choice]
        return monster_class()