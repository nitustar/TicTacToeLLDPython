from src.helper.Stratergy.BotFactory import BotFactory
from src.models.PlayerType import PlayerType
from src.models.players import Player


class Bot(Player):
    def __init__(self, player_id: int, name: str, symbol, difficulty):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.stgy = BotFactory.getBot(self.difficulty)

    def decide_cell(self, board):
        return self.stgy.decide_move(board)