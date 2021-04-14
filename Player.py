from random import randint, shuffle


class Player:
    name: str
    __hands = ()
    __score: int

    def __init__(self, name, maquina=False):
        self.name = name
        if maquina:
            self.__sort_hands()
        self.__score = 0

    def __sort_hands(self):
        nums = []
        for i in range(3):
            nums.append(randint(1, 3))
        self.__hands = tuple(nums)

    def add_hand(self, hand: int):
        before = list(self.__hands)
        before.append(hand)
        self.__hands = tuple(before)

    def get_hands(self) -> tuple:
        return self.__hands

    def get_hand_by_round(self, n_round: int) -> int:
        return self.__hands[n_round - 1]

    def add_score(self):
        self.__score += 1

    def get_score(self) -> int:
        return self.__score
