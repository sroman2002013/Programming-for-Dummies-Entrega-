from soldier_action import SoldierAction

class ReloadAction(SoldierAction):

    def execute(self, soldier):
        soldier.weapon.reload()
