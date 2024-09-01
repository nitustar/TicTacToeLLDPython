from src.helper.GameBuilder import GameBuilder
from src.models.GameStatus import GameStatus
from src.models.board import Board


class Game:
    def __init__(self, dimension, players, winning_startergies):
        self.players = players
        self.winning_startergies = winning_startergies
        self.Board = Board(dimension)
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.INPROGRESSED


    @staticmethod
    def gameBuilder():
        return GameBuilder()
