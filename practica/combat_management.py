import random




class CombatManagement:
    def __init__(self, soldier: dict, monster_team: list):

        self.soldier = soldier
        self.monster_team = monster_team


    def recharge_weapon(self):
        if self.soldier["state"] == "standard":
            print("Hello")

        elif self.soldier["state"] == "cursed":
            print("Hello")
            print("Cursed! losing HP")
            self.soldier["hp"] -= 50

        elif self.soldier["state"] == "scared":
            print("Hello")
            choice = random.choice([True, False])
            if not choice:
                print("Scared, cant attack")
                return
        elif self.soldier["state"] == "troll":
            print("xfmqwekeqqkq")

        if self.soldier["weapon"] == "Shot Gun":
            self.soldier["munition"] += 1
        else:
            self.soldier["munition"] = self.soldier["max_munition"]

    def try_critical_shot(self, monster_to_shot:dict):


        if self.soldier["state"] == "standard":
            print("Hello")

        elif self.soldier["state"] == "cursed":
            print("Hello")
            print("Cursed! losing HP")
            self.soldier["hp"] -= 50

        elif self.soldier["state"] == "scared":
            print("Hello")
            choice = random.choice([True, False])
            if not choice:
                print("Scared, cant attack")
                return
        elif self.soldier["state"] == "troll":
            print("xfmqwekeqqkq")

        if self.soldier["munition"] <= 0:
            print("No Munition!!!!")
            return

        if self.soldier["weapon"] == "Gun":
            self.soldier["munition"] -= 1
            choice = random.choice([True, False])
            if not choice:
                print("Critical Failed!")
                return
            monster_to_shot["hp"]-= 60
        elif self.soldier["weapon"] == "Shot Gun":
            self.soldier["munition"] -= 1
            choice = random.choice([True, False])
            if not choice:
                print("Critical Failed!")
                return
            monster_to_shot["hp"] -= 120
        elif self.soldier["weapon"] == "Machine Gun":
            self.soldier["munition"] -= 3
            choice = random.choice([True, False])
            if not choice:
                print("Critical Failed!")
                return
            monster_to_shot["hp"] -= random.randint(1, 3) * 60

        if monster_to_shot["hp"] <= 0:
            self.monster_team.remove(monster_to_shot)

    def soldier_shot(self, monster_to_shot: dict):
        if self.soldier["state"] == "standard":
            print("Hello")

        elif self.soldier["state"] == "cursed":
            print("Hello")
            print("Cursed! losing HP")
            self.soldier["hp"] -= 50

        elif self.soldier["state"] == "scared":
            print("Hello")
            choice = random.choice([True, False])
            if not choice:
                print("Scared, cant attack")
                return
        elif self.soldier["state"] == "troll":
            print("xfmqwekeqqkq")

        if self.soldier["munition"] <= 0:
            print("No Munition!!!!")
            return

        if self.soldier["weapon"] == "Gun":
            self.soldier["munition"] -= 1
            monster_to_shot["hp"] -= 30
        elif self.soldier["weapon"] == "Shot Gun":
            self.soldier["munition"] -= 1
            monster_to_shot["hp"] -= 60
        elif self.soldier["weapon"] == "Machine Gun":
            self.soldier["munition"] -= 3
            monster_to_shot["hp"] -= random.randint(1, 3) * 30

        if monster_to_shot["hp"] <= 0:
            self.monster_team.remove(monster_to_shot)

    def monsters_attack(self, monster: dict):
        damage = monster["attack_damage"]
        if monster["monster_type"] == "Troll":
            if monster["hp"] <= 50:
                print("DOUBLE TROLL ATTACK")
                damage *= 2

        self.soldier["hp"] -= damage
        print(monster["monster_type"] + " is doing " + str(damage) + " damage")

    def special_attack(self, monster:dict):
        monster_type = monster["monster_type"]
        if monster_type == "Troll":
            print("Applying troll state")
            self.soldier["state"] = "troll"
        elif monster_type == "Daemon":
            print("Applying cursed state")
            self.soldier["state"] = "cursed"
        elif monster_type == "Ghost":
            print("Applying scared state")
            self.soldier["state"] = "scared"
