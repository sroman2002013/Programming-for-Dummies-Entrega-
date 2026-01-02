from monster_action import MonsterAction

class SpecialAttackAction(MonsterAction):
    def __init__(self, monster):
        self.monster = monster
    
    def execute(self, soldier):
        self.monster.special_attack(soldier)