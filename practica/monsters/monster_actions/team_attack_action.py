from monsters.monster_actions.monster_action import MonsterAction

class TeamAttackAction(MonsterAction):
    def __init__(self, monster_team):
        self.monster_team = monster_team
    
    def execute(self, soldier):
        for monster in self.monster_team.monsters:
            monster.attack(soldier)
            