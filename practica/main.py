from combat_management import CombatManagement
from constants import WEAPONS, MONSTERS, SOLDIER_ACTIONS, MONSTER_ACTIONS


if __name__ == "__main__":
    monsters_types = {
        "Troll": {
            "hp": 90,
            "attack_damage": 30
        },

        "Daemon": {
            "hp": 90,
            "attack_damage": 40
        },

        "Ghost": {
            "hp": 130,
            "attack_damage": 30
        }
    }

    print("Lets configure our soldier: ")
    weapon_n = input("Choose weapon {1: Gun, 2: Shot Gun, 3: Machine Gun}: ")
    while weapon_n not in WEAPONS.keys():
        weapon_n = input("Choose weapon {1: Gun, 2: Shot Gun, 3: Machine Gun}: ")

    weapon = WEAPONS[weapon_n]

    name = str(input("What is your name?: "))
    if weapon == "Gun":
        max_munition = 10
    elif weapon == "Shot Gun":
        max_munition = 3
    elif weapon == "Machine Gun":
        max_munition = 15
    else:
        raise ValueError("Not valid weapon")
    soldier = {"name": name, "weapon": weapon, "hp": 1000, "state": "standard", "max_munition": max_munition,
               "munition": max_munition}

    monsters = []
    print("Lets choose the monsters team, they will be three monsters")
    monster_number = input("Choose monster 1 {1: Troll, 2: Ghost, 3: Daemon}: ")
    while monster_number not in MONSTERS.keys():
        monster_number = input("Choose monster 2 {1: Troll, 2: Ghost, 3: Daemon}: ")
    monster_type = MONSTERS[monster_number]
    selected_monster = {"monster_type": monster_type, "hp": monsters_types[monster_type]["hp"],
                        "attack_damage": monsters_types[monster_type]["attack_damage"]}
    monsters.append(selected_monster)

    monster_number = input("Choose monster 2 {1: Troll, 2: Ghost, 3: Daemon}: ")
    while monster_number not in MONSTERS.keys():
        monster_number = input("Choose monster 2 {1: Troll, 2: Ghost, 3: Daemon}: ")
    monster_type = MONSTERS[monster_number]
    selected_monster = {"monster_type": monster_type, "hp": monsters_types[monster_type]["hp"],
                        "attack_damage": monsters_types[monster_type]["attack_damage"]}
    monsters.append(selected_monster)

    monster_number = input("Choose monster 3 {1: Troll, 2: Ghost, 3: Daemon}: ")
    while monster_number not in MONSTERS.keys():
        monster_number = input("Choose monster 3 {1: Troll, 2: Ghost, 3: Daemon}: ")
    monster_type = MONSTERS[monster_number]
    selected_monster = {"monster_type": monster_type, "hp": monsters_types[monster_type]["hp"],
                        "attack_damage": monsters_types[monster_type]["attack_damage"]}
    monsters.append(selected_monster)

    combat_management = CombatManagement(soldier=soldier, monster_team=monsters)

    while True:
        print("Soldier " + soldier["name"] + "!!. Your hp is " + str(soldier["hp"]) + " and your remaining munition " + str(
            soldier["munition"]))
        soldier_action = input("Choose action {1: Shot, 2: Recharge, 3: Try Critical Shot}: ")
        while soldier_action not in SOLDIER_ACTIONS.keys():
            soldier_action = input("Choose action {1: Shot, 2: Recharge, 3: Try Critical Shot}: ")
        if SOLDIER_ACTIONS[soldier_action] == "Shot":
            for i in range(1, len(monsters) + 1):
                print(str(i) + ": " + monsters[i - 1]["monster_type"] + ": " + str(monsters[i - 1]["hp"]) + " HP")
            enemy_to_shoot_number = input(
                "Choose monster to attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")
            while enemy_to_shoot_number not in [str(i) for i in range(1, len(monsters) + 1)]:
                enemy_to_shoot_number = input(
                    "Choose monster to attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")
            enemy_to_shoot = monsters[int(enemy_to_shoot_number) - 1]
            combat_management.soldier_shot(monster_to_shot=enemy_to_shoot)
            print(enemy_to_shoot["monster_type"] + " has " + str(enemy_to_shoot["hp"]) + " remaining")
            if len(monsters) == 0:
                print("Soldier wins")
                break
        elif SOLDIER_ACTIONS[soldier_action] == "Try Critical Shot":
            for i in range(1, len(monsters) + 1):
                print(str(i) + ": " + monsters[i - 1]["monster_type"] + ": " + str(monsters[i - 1]["hp"]) + " HP")
            enemy_to_shoot_number = input(
                "Choose monster to attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")
            while enemy_to_shoot_number not in [str(i) for i in range(1, len(monsters) + 1)]:
                enemy_to_shoot_number = input(
                    "Choose monster to attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")
            enemy_to_shoot = monsters[int(enemy_to_shoot_number) - 1]
            combat_management.try_critical_shot(monster_to_shot=enemy_to_shoot)
            print(enemy_to_shoot["monster_type"] + " has " + str(enemy_to_shoot["hp"]) + " remaining")
            if len(monsters) == 0:
                print("Soldier wins")
                break

        elif SOLDIER_ACTIONS[soldier_action] == "Recharge":
            combat_management.recharge_weapon()

        print("Monsters!! This your state")
        for i in range(1, len(monsters) + 1):
            print(str(i) + ": " + monsters[i - 1]["monster_type"] + ": " + str(monsters[i - 1]["hp"]) + " HP")
        monsters_action = input("Choose action {1: All Team Attack, 2: Special Attack}: ")
        while monsters_action not in MONSTER_ACTIONS.keys():
            monsters_action = input("Choose action {1: All Team Attack, 2: Special Attack}}: ")
        if MONSTER_ACTIONS[monsters_action] == "All Team Attack":
            for monster in monsters:
                combat_management.monsters_attack(monster=monster)
            if soldier["hp"] <= 0:
                print("Monsters win")
                break
        elif MONSTER_ACTIONS[monsters_action] == "Special Attack":
            for i in range(1, len(monsters) + 1):
                print(str(i) + ": " + monsters[i - 1]["monster_type"] + ": " + str(monsters[i - 1]["hp"]) + " HP")
            monster_special_number = input(
                "Choose monster to special attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")
            while monster_special_number not in [str(i) for i in range(1, len(monsters) + 1)]:
                monster_special_number = input(
                    "Choose monster to special attack! " + str([str(i) for i in range(1, len(monsters) + 1)]) + ": ")

            monster_special = monsters[int(monster_special_number) - 1]
            combat_management.special_attack(monster=monster_special)
