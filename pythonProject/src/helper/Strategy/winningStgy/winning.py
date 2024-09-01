from abc import ABC, abstractmethod


class Winning(ABC):
    @abstractmethod
    def check_winner(self, cell, player):
        pass

    def undo_handler(self, cell, player):
        pass
