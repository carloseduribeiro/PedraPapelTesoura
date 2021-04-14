from Player import Player


class Round:
    winner: Player

    def __init__(self, p1: Player, p2: Player, num_round):
        self.player_1 = p1
        self.player_2 = p2
        self.num_round = num_round

    def set_winner(self, winner: Player):
        self.winner = winner
        self.winner.add_score()

    def start(self):
        hand_p1 = self.player_1.get_hand_by_round(self.num_round)
        hand_p2 = self.player_2.get_hand_by_round(self.num_round)

        # PEDRA | PAPEL | TESOURA
        # 1 | 2 | 3
        if hand_p1 == 1 and hand_p2 == 3:
            # PEDRA vs TESOURA = PEDRA
            self.set_winner(self.player_1)
        elif hand_p1 == 1 and hand_p2 == 2:
            # PEDRA vs PAPEL = PAPEL
            self.set_winner(self.player_2)

        elif hand_p1 == 2 and hand_p2 == 1:
            # PAPEL vs PEDRA = PAPEL
            self.set_winner(self.player_1)
        elif hand_p1 == 2 and hand_p2 == 3:
            # PAPEL vs TESOURA = TESOURA
            self.set_winner(self.player_2)

        elif hand_p1 == 3 and hand_p2 == 2:
            # TESOURA vs PAPEL = TESOURA
            self.set_winner(self.player_1)
        elif hand_p1 == 3 and hand_p2 == 1:
            # TESOURA vs PEDRA = PEDRA
            self.set_winner(self.player_2)
        else:
            self.set_winner(Player("Empate"))

    def get_winner(self) -> Player:
        return self.winner
