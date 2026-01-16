from combat import CombatManager
from soldier.soldier_factory import SoldierFactory
from monsters.monster_factory import MonsterFactory

class Game:
    def __init__(self):
        self.wins = 0
        

    def get_difficulty_settings(self):
        name = "Fácil"
        hp = 1000
        m_count = 3
        force_gun = False

        if self.wins >= 5: 
            name = "Difícil"
            hp = hp/2
            m_count = 4
            force_gun = True
        elif self.wins >= 3: 
            name = "Media"
            hp = hp/2
            m_count = 4
        
        return name, hp, m_count, force_gun
    
    def run(self):
        print("=== WELCOME TO MONSTER SLAYER ===")
        
        player_name = input("What is your name, soldier?: ")
        
        playing = True
        while playing:
            diff_name, hp, m_count, force_gun = self.get_difficulty_settings()
            
            print(f"\n" + "="*45)
            print(f"COMBAT #{self.wins + 1} | DIFFICULTY: {diff_name}")
            print(f"Soldier: {player_name} | Starting HP: {hp}")
            print("="*45)

            
            soldier = SoldierFactory.create_soldier(player_name, hp, force_gun)
            
            monster_team = MonsterFactory.create_team(m_count)
            
            combat = CombatManager(soldier, monster_team)
            winner = combat.run_combat()
            
            if winner == "soldier":
                self.wins += 1
                print(f"\nVICTORY! You have won {self.wins} combat(s).")
                if input("Prepare for the next challenge? (y/n): ").lower() != 'y':
                    playing = False
            else:
                print(f"\nDEFEAT... You died in round {self.wins + 1}.")
                playing = False

        print(f"\n=== FINAL SCORE ===")
        print(f"Soldier: {player_name}")
        print(f"Total Victories: {self.wins}")

if __name__ == "__main__":
    game = Game()
    game.run()