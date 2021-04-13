from random import randint, shuffle


class Player:
    name: str
    __hands = ()

    def __init__(self, name):
        self.name = name
        self.__sort_hands()

    def __sort_hands(self):
        nums = []
        for i in range(3):
            nums.append(randint(1, 3))
        self.__hands = tuple(nums)

    def get_hands(self) -> tuple:
        return self.__hands
