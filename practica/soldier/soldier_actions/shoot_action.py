from soldier_action import SoldierAction

class ShootAction(SoldierAction):
    
    def __init__(self, target):
        self.target = target

    def execute(self, soldier):
        soldier.weapon.shoot(self.target)