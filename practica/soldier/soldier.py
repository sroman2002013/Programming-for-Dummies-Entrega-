class Soldier:
    def __init__(self, hp, weapon, state):
        self.hp = hp
        self.weapon = weapon
        self.state = state

    def take_damage(self, damage: int):
        self.hp -= damage
        # TODO: print???


    def perform_action(self, action):
        self.state.on_turn_start(self)

        if not self.state.can_act():
            # TODO: print???
            return
        
        action.execute(self)


    def set_state(self, new_state):
        self.state = new_state
