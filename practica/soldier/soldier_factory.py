from soldier import Soldier
from soldier_states.soldier_state import StandardState
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
    def create_soldier(name="Accenture enjoyer") -> Soldier:        
        print("Choose weapon {1: Gun, 2: Shot Gun, 3: Machine Gun}")
        weapon_choice = input("Select weapon: ")
        
        while weapon_choice not in SoldierFactory.WEAPON_MAP:
            print("Invalid weapon selection.")
            weapon_choice = input("Select weapon {1: Gun, 2: Shot Gun, 3: Machine Gun}: ")
            
        weapon_class = SoldierFactory.WEAPON_MAP[weapon_choice]
        weapon_instance = weapon_class()
        
        return Soldier(name=name, hp=1000, weapon=weapon_instance, state=StandardState())