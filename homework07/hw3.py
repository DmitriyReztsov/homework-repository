"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import defaultdict
from typing import List


def validate(board):
    check = set()
    for sub in board:
        check |= set(sub)
    return len(check) == 2 or len(check) == 3 and "-" in check


def check_win_line(ch_dict):
    if len(ch_dict) == 3 or (len(ch_dict) < 3 and "-" in ch_dict):
        return "unfinished!"
    if len(ch_dict) == 2:
        return "draw!"
    if len(ch_dict) == 1:
        for key, _ in ch_dict.items():
            return f"{key} wins!"


def check_win_board(result: List) -> str:
    return_result = ""
    for value in result:
        if "win" in value:
            return value
        if "unfinished!" in value:
            return_result = "unfinished!"
        if "draw!" in value and "unfinished!" not in return_result:
            return_result = "draw!"
    return return_result


def parse_combinations(boards: List[List]) -> str:
    result = []
    for line in boards:
        chars = defaultdict(int)
        for char in line:
            chars[char] += 1
        result.append(check_win_line(chars))
    return check_win_board(result)


def tic_tac_toe_checker(board: List[List]) -> str:
    if not validate(board):
        print("ERROR : you're playing smth else, not Tic-Tac-Toe !")
        raise SystemError
    board_vert = [[board[i][j] for i in range(3)] for j in range(3)]
    board_diag = [[board[i][i] for i in range(3)], [board[2 - i][i] for i in range(3)]]
    result_horizontal = parse_combinations(board)
    result_vertical = parse_combinations(board_vert)
    result_diagonal = parse_combinations(board_diag)
    return check_win_board([result_horizontal, result_vertical, result_diagonal])


if __name__ == "__main__":
    a = tic_tac_toe_checker([["o", "x", "o"], ["o", "x", "o"], ["x", "o", "x"]])
