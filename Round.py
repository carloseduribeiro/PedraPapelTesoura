from Player import Player


class Round:
    winner: Player
    hand_p1: int
    hand_p2: int
    hands = {
        1: "PEDRA",
        2: "PAPEL",
        3: "TESOURA",
    }

    def __init__(self, p1: Player, p2: Player, num_round: int):
        self.winner = Player("EMPATE")
        self.player_1 = p1
        self.player_2 = p2
        self.num_round = num_round

    def start(self):
        self.hand_p1 = self.player_1.get_hands()[self.num_round]
        self.hand_p2 = self.player_2.get_hands()[self.num_round]

        # PEDRA | PAPEL | TESOURA
        # 1 | 2 | 3

        if self.hand_p1 == 1 and self.hand_p2 == 3:
            # PEDRA vs TESOURA = PEDRA
            self.winner = self.player_1
        elif self.hand_p1 == 1 and self.hand_p2 == 2:
            # PEDRA vs PAPEL = PAPEL
            self.winner = self.player_2

        if self.hand_p1 == 2 and self.hand_p2 == 1:
            # PAPEL vs PEDRA = PAPEL
            self.winner = self.player_1
        elif self.hand_p1 == 2 and self.hand_p2 == 3:
            # PAPEL vs TESOURA = TESOURA
            self.winner = self.player_2

        elif self.hand_p1 == 3 and self.hand_p2 == 2:
            # TESOURA vs PAPEL = TESOURA
            self.winner = self.player_1
        elif self.hand_p1 == 3 and self.hand_p2 == 1:
            # TESOURA vs PEDRA = PEDRA
            self.winner = self.player_2

    def get_winner(self):
        return self.winner
