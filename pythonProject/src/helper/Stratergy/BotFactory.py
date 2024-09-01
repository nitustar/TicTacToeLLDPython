#  add abc class also..
from src.helper.Stratergy.botStgy.Easy import Easy
from src.models.BotDificulty import BotDificulty


class BotFactory:
    @staticmethod
    def getBot(difficulty):
        if difficulty == BotDificulty.EASY:
            return Easy()

