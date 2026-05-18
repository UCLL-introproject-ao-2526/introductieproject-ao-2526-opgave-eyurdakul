from enum import Enum

class Symbols(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4

class SoundLibrary(Enum):
    CARD = 1
    CHIP = 2
    WIN = 3
    LOSE = 4
    CLICK = 5
    SHUFFLE = 6

class Result(Enum):
    PLAYER_ABOVE_21 = 1
    PLAYER_WINS = 2
    DEALER_WINS = 3
    TIE_GAME = 4
