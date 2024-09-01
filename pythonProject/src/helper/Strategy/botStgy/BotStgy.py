from abc import ABC, abstractmethod

class BotStgy(ABC):

    @abstractmethod
    def decide_move(self, board):
        pass

    def undo_handler(self, board):
        pass