from soldier.soldier import Soldier
from soldier.soldier_actions.soldier_action import SoldierAction
from soldier.soldier_actions.shoot_action import ShootAction
from soldier.soldier_actions.reload_action import ReloadAction
from soldier.soldier_actions.critical_shot_action import CriticalShotAction

from monsters.monster_team import MonsterTeam
from monsters.monster_actions.monster_action import MonsterAction
from monsters.monster_actions.team_attack_action import TeamAttackAction
from monsters.monster_actions.special_attack_action import SpecialAttackAction

class CombatManager:
    def __init__(self, soldier: Soldier, monsters_team: MonsterTeam):
        self.soldier = soldier
        self.monsters_team = monsters_team

    def is_finished(self) -> bool:
        return not self.soldier.is_alive() or self.monsters_team.all_dead()
    
    def get_winner(self) -> str:
        if self.soldier.is_alive():
            return "soldier"
        else:
            return "monsters"

    def display_soldier_info(self):
        print(f"Soldier {self.soldier.name}!!. Your hp is {self.soldier.hp} and your remaining ammunition {self.soldier.weapon.ammunition}")

    def display_monsters_info(self):
        print("Monsters!! This is your state")
        for i, monster in enumerate(self.monsters_team.monsters, 1):
            print(f"{i}: {monster.__class__.__name__}: {monster.hp} HP")

    def ask_soldier_action(self) -> SoldierAction:
        
        soldier_action = input("Choose action {1: Shot, 2: Recharge, 3: Try Critical Shot}: ")
        
        if soldier_action == "1":
            self.display_monsters_info()
            idx = int(input("Choose monster to attack: ")) - 1
            return ShootAction(self.monsters_team.monsters[idx])
        elif soldier_action == "2":
            return ReloadAction()
        elif soldier_action == "3":
            self.display_monsters_info()
            idx = int(input("Choose monster to attack: ")) - 1
            return CriticalShotAction(self.monsters_team.monsters[idx])
        else:
            return self.ask_soldier_action()

    def ask_monster_action(self) -> MonsterAction:
        
        monsters_action = input("Choose action {1: All Team Attack, 2: Special Attack}: ")
        
        if monsters_action == "1":
            return TeamAttackAction(self.monsters_team)
        else: 
            self.display_monsters_info()
            idx = int(input("Choose monster to perform special attack: ")) - 1
            return SpecialAttackAction(self.monsters_team.monsters[idx])

    def soldier_turn(self):
        if self.is_finished():
            return
        
        action = self.ask_soldier_action()
        self.soldier.perform_action(action)
        self.monsters_team.remove_dead()

    def monster_turn(self):
        if self.is_finished():
            return
        
        action = self.ask_monster_action()
        action.execute(self.soldier)
        self.monsters_team.remove_dead()

    def run_combat(self):
        print("=== Combat Start ===")
        while not self.is_finished():
            self.display_soldier_info()
            self.soldier_turn()
            if self.is_finished():
                break
            self.display_monsters_info()
            self.monster_turn()
        
        winner = self.get_winner()
        print(f"{winner.capitalize()} won!")
        return winner