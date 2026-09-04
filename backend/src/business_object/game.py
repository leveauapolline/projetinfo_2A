from datetime import datetime

from .player import Player


class Game:
    def __init__(self, player1: Player, player2: Player, game_mode: str, winner: Player, description: str, timestamp: datetime):
        self.id_game = None,
        self.p1 = player1,
        self.p2 = player2,
        self.game_mode = game_mode,
        self.winner = winner,
        self.description = description,
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.game_mode} between {self.p1.username} and {self.p2.username}. Winner : {self.winner.username}"
