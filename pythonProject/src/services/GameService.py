from src.models.CellStatus import CellStatus
from src.models.GameStatus import GameStatus


class GameService:

    def start_game(self, size, players, winning_stg):
        from src.models.Game import Game
        game = Game.gameBuilder().set_players(players).set_dimension(size).set_winning_startergies(winning_stg).build()
        return game

    def display_game(self, game):
        game.Board.print_board()

    def take_move(self, game):
        current_player = game.players[game.next_turn]
        cell = current_player.decide_cell(game.Board)
        cell.player = current_player
        cell.status = CellStatus.FILLED
        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.gameStatus = GameStatus.COMPLETED
            game.winner = current_player
        elif len(game.moves) == game.Board.board_size * game.Board.board_size:
            game.gameStatus = GameStatus.DRAW

        game.next_turn +=1
        game.next_turn %= len(game.players)

    def check_winner(self, game, cell):
        return any(ws.check_winner(cell, game.Board,) for ws in game.winning_startergies)

    def undo(self, game):
        if not game.moves:
            print("No moves left to undo")
            return

        cell = game.moves.pop()

        for ws in game.winning_startergies:
            ws.undo_handle(cell, game.Board)
        cell.status = CellStatus.EMPTY
        cell.player = None

        game.next_turn -=1
        game.next_turn %= len(game.players)
