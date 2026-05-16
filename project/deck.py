import constants
import random

from card import Card
from enums import Symbols

class Deck:

    def create(self):
        self._deck = list()
        self.ranks = list(constants.RANKS)
        for symbol in Symbols:
            for rank in self.ranks:
                card = Card(rank, symbol)
                self._deck.append(card)
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop()