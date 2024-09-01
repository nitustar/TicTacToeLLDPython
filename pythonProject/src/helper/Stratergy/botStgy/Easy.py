from src.helper.Stratergy.botStgy.BotStgy import BotStgy
from src.models.CellStatus import CellStatus


class Easy(BotStgy):
    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None
