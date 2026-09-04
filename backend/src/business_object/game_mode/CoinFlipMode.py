from datetime import datetime
from random import randint

from .game import Game
from .GameMode import GameMode
from .player import Player


class CoinFlipMode(GameMode):
    def play(self, p1: Player, p2: Player) -> Game:
        score1 = randint(1, 6)
        score2 = randint(1, 6)
        if score1 > score2:
            winner = p1
        elif score2 > score1:
            winner = p2
        else:
            winner = None
        description = f"{p1.username} scored {score1} and {p2.username} scored {score2}"
        return Game(p1, p2, "coinflip", winner, description, datetime.now())
