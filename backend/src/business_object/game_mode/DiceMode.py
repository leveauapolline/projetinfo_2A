from datetime import datetime
from random import choice as fchoice

from .game import Game
from .GameMode import GameMode
from .player import Player


class DiceMode(GameMode):
    def play(self, p1: Player, p2: Player, choice: str) -> Game:
        result = fchoice(["heads", "tails"])
        winner = p1 if result == choice else p2
        description = ""
        return Game(p1, p2, "dice", winner, description, datetime.now())
