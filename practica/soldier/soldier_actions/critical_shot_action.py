from soldier.soldier_actions.soldier_action import SoldierAction
import random

class CriticalShotAction(SoldierAction):

    def __init__(self, target):
        self.target = target

    def execute(self, soldier):
        damage_multiplier = random.choice([0, 2])
        soldier.weapon.shoot(self.target, damage_multiplier)