import sys
from copy import deepcopy
from constants import NUM_TO_WIN

sys.setrecursionlimit(5000)


def minimax(board, depth, max_player, game, alpha, beta, num_to_win=NUM_TO_WIN):
    if depth == 0 or game.check_for_win(board, num_to_win)[0]:
        return (board.evaluate(num_to_win, num_to_win), board)

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(board, 'O'):
            evaluation = minimax(move, depth-1, False, game, alpha, beta, num_to_win)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
            alpha = max(alpha, max_eval)
            if alpha > beta:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(board, 'X'):
            evaluation = minimax(move, depth-1, True, game, alpha, beta, num_to_win)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
            beta = min(beta, min_eval)
            if alpha > beta:
                break
        return min_eval, best_move


def get_all_moves(board, symbol):
    moves = []

    for row_index, row in enumerate(board.board):
        for column_index, symb in enumerate(row):
            if symb is None:
                temp_board = deepcopy(board)
                temp_board.board[row_index][column_index] = symbol
                moves.append(temp_board)

    return moves
