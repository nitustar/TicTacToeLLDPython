# create abc class also. and then inherit it in the botStgy.py and winning.py
from src.helper.Strategy.botStgy.Easy import Easy
from src.models.BotDifficulty import BotDifficulty


class BotFactory:

    @staticmethod
    def getBot(difficulty):
        if difficulty == BotDifficulty.EASY:
            return Easy()


        # elif difficulty == 'medium':
        #     return Medium()
        # elif difficulty == 'hard':
        #     return Hard()
        # else:
        #     return None