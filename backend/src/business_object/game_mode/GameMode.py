from abc import ABC, abstractmethod

from .player import Player


class GameMode(ABC):
    @abstractmethod
    def play(p1: Player, p2: Player):
        pass
