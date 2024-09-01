from src.CustomExceptions.InvalidPlayerException import InvalidPlayerException


class GameBuilder:
    def __init__(self):
        self.dimension = None
        self.players = None
        self.winning_startergies = None

    def set_dimension(self, dimension):
        self.dimension = dimension
        return self

    def set_players(self, players):
        self.players = players
        return self

    def set_winning_startergies(self, winning_startergies):
        self.winning_startergies = winning_startergies
        return self


    def validate(self):
        if len(self.players) > self.dimension - 1:
            raise InvalidPlayerException()

    def build(self):
        from src.models.Game import Game
        self.validate()
        return Game(self.dimension, self.players, self.winning_startergies)
