from soldier.soldier import Soldier
from soldier.soldier_states.normal_state import NormalState
from weapons.gun import Gun
from weapons.shotgun import Shotgun
from weapons.machinegun import Machinegun

class SoldierFactory:
    
    # Map input keys to Weapon Classes (Strategy Pattern)
    WEAPON_MAP = {
        "1": Gun,
        "2": Shotgun,
        "3": Machinegun
    }

    @staticmethod
    def create_soldier(name, hp, force_gun=False):
        if force_gun:
            print(f"HARD MODE ACTIVE: {name}, you are restricted to using the 'Gun' only!")
            weapon = Gun()
        else:
            
            print("{1: Gun, 2: Shot Gun, 3: Machine Gun}")
            choice = input("Selection: ")
            
            weapon = SoldierFactory.WEAPON_MAP.get(choice, Gun)()
        
        return Soldier(name=name, weapon=weapon, hp=hp)