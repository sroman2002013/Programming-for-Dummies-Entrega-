from combat import CombatManager
from soldier.soldier_factory import SoldierFactory
from monsters.monster_factory import MonsterFactory

class Game:
    def __init__(self):
        self.wins = 0
        self.difficulty = 1
    
    def run(self):
        print("=== Welcome to Monster Slayer ===")
        
        soldier = SoldierFactory.create_soldier()
        
        while soldier.is_alive():
            print(f"\n=== Combat #{self.wins + 1} (Difficulty: {self.difficulty}) ===")
            
            if self.wins >= 2:  
                soldier.hp = soldier.hp // 2
                print(f"Hard mode! Soldier HP halved: {soldier.hp}")
                monster_count = 4
            else:
                monster_count = 3
            
            if self.wins >= 4:  
                print("Extreme mode! Only Gun allowed.")
                # soldier.weapon = Gun()
            
            monster_team = MonsterFactory.create_team(monster_count)
            
            combat = CombatManager(soldier, monster_team)
            winner = combat.run_combat()
            
            if winner == "soldier":
                self.wins += 1
                self.difficulty = (self.wins // 3) + 1
                print(f"Victory! Total wins: {self.wins}")
                
                if soldier.is_alive():
                    continue_game = input("Continue to next combat? (y/n): ").lower()
                    if continue_game != 'y':
                        break
            else:
                print("Game Over!")
                break
        
        print(f"\n=== Final Score ===")
        print(f"Total victories: {self.wins}")
        print(f"Maximum difficulty reached: {self.difficulty}")