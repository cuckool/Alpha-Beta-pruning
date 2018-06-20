class InterfaceGames2Player:
    def __init__(self, **kwargs):
        raise NotImplementedError('You should have overriden this method. You have to be able to clone a game state and'
                                  ' to generate one.')

    def generate_children(self):
        raise NotImplementedError('You should have overriden this method.')

    def personal_hash(self):
        raise NotImplementedError('You should have overriden this method.')

    def is_maximizing_player_turn_now(self):
        raise NotImplementedError('You should have overriden this method.')


class Heuristics:
    def generate_score(self, game_state: InterfaceGames2Player):
        raise NotImplementedError('You should have implemented this.')