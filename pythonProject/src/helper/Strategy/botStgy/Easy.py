from src.helper.Strategy.botStgy.BotStgy import BotStgy


class Easy(BotStgy):

    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == cell.CellStatus.EMPTY:
                    return cell
        return None

