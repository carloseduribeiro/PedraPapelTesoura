from Round import Round
from Player import Player


class Game:
    # rounds = {}
    rounds = {}
    player_1: Player
    player_2: Player

    def __init__(self, name_p1: str, name_p2: str):
        self.player_1 = Player(name_p1)
        self.player_2 = Player(name_p2)

    def start(self):
        for i in range(3):
            round_game = Round(self.player_1, self.player_2, i)
            round_game.start()
            self.rounds[i + 1] = round_game

    def get_rounds(self) -> dict:
        return self.rounds
