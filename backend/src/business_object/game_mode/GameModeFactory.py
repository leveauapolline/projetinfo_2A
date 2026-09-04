from .CoinFlipMode import CoinFlipMode
from .DiceMode import DiceMode
from .GameMode import GameMode
from .player import Player


class GameModeFactory:
     SUPPORTED_MODES = {
        "coinflip": CoinFlipMode,
        "dice": DiceMode,
    }

    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        mode_class = cls.SUPPORTED_MODES.get(game_mode.lower())

        if mode_class:
            return mode_class()

        raise ValueError(f"Game mode '{game_mode}' is not supported.")
