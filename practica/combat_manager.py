from monsters.monster import Monster
from constants import WEAPONS, MONSTERS, SOLDIER_ACTIONS, MONSTER_ACTIONS

class CombatManager:

    def __init__(self, soldier, monsters_team):
        self.soldier = soldier
        self.monsters_team = monsters_team

    def is_finished(self) -> bool:
        return not self.soldier.is_alive() or self.monsters_team.all_dead()
    
    def get_winner(self):
        if self.soldier.is_alive():
            print("Soldier won")
        else:
            print("Soldier is a loser, monster won")

    def display_soldier_info(self):
         print("Soldier " + self.soldier + "!!. Your hp is " + str(self.soldier["hp"]) + " and your remaining munition " + str(self.soldier.weapon.ammunition))



    def display_monsters_info(self):
        print("Monsters!! This is your state")
        for i in range(1, len(self.monsters_team) + 1):
            print(str(i) + ": " + self.monsters_team[i - 1].__name__ + ": " + str(self.monsters_team[i - 1].hp) + " HP")


    def ask_soldier_action(self):
        soldier_action = input("Choose action {1: Shot, 2: Recharge, 3: Try Critical Shot}: ")
        while soldier_action not in SOLDIER_ACTIONS.keys():
            soldier_action = input("Choose action {1: Shot, 2: Recharge, 3: Try Critical Shot}: ")
        return soldier_action
    
    def ask_monster_to_attack(self) -> Monster:
        monster_to_attack = input("Choose monster to attack: " + str([str(i) for i in range(1, len(self.monsters_team) + 1)]) + ": ")
        while monster_to_attack not in [str(i) for i in range(1, len(self.monsters) + 1)]:
            monster_to_attack = input("Choose monster to attack: " + str([str(i) for i in range(1, len(self.monsters_team) + 1)]) + ": ")
        return self.monsters_team[monster_to_attack]

    def ask_monster_action(self): 
        monsters_action = input("Choose action {1: All Team Attack, 2: Special Attack}: ")
        while monsters_action not in MONSTER_ACTIONS.keys():
            monsters_action = input("Choose action {1: All Team Attack, 2: Special Attack}}: ")
        return monsters_action


    def soldier_turn(self, action):
        if self.is_finished():
            return
        

        

        
        self.soldier.perform_action(action)
        self.monsters_team.remove_dead()

    def monster_turn(self, action):
        if self.is_finished():
            return
        
        action.execute(self)