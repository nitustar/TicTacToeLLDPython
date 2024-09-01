from src.controller.GameController import GameController
from src.helper.Stratergy.winningStgy.diagonalWS import DiagonalWS
from src.models.Bot import Bot
from src.models.BotDificulty import BotDificulty
from src.models.GameStatus import GameStatus
from src.models.PlayerType import PlayerType
from src.models.Symbol import Symbol
from src.models.players import *
from src.services.GameService import GameService

if __name__ == '__main__':

    Gs = GameService()
    gc = GameController(Gs)

    dimensions = 3

    players = [
        Player("Nitesh", 1, PlayerType.HUMAN, Symbol("x")),
        Bot(2, "Mohit", Symbol("y"), BotDificulty.EASY),
    ]

    winning = [DiagonalWS()]

    game = gc.start_game(dimensions, players, winning)
    # display board..

    gc.display_board(game)

    #  until game in progress take input..

    while game.gameStatus == GameStatus.INPROGRESSED:
        gc.take_move(game)
        gc.display_board(game)
        undo_answer = input("Do you want to undo? If yes, press 1: ")
        if undo_answer == "1":
            print("Undo...")
            gc.undo_move(game)
            gc.display_board(game)

    # show end game msg..
    if game.gameStatus == GameStatus.COMPLETED:
        print(f"Winner: {game.winner.name}")
    elif game.gameStatus == GameStatus.DRAW:
        print(f"Draw!")

# TODO: 1. Medium and hard bot strgy..
#       2. Winning stgy row and col..
#       3. Implement multiple undos..
#       4. undo as snapshot..
#       5. try other winning algos..
