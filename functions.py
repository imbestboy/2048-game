import random


def get_number(input_text: str, max_number: int, min_number: int) -> int:
    """get_number get number from user by input function

    Arguments:
        input_text {str} -- text to show input function
        max_number {int} -- maximum number user can enter
        max_number {int} -- minimum number user can enter

    Returns:
        int -- entered user number
    """
    while True:
        number = input(input_text)
        if (
            number.isnumeric()
            and int(number) <= max_number
            and int(number) >= min_number
        ):
            return int(number)
        elif not number.isnumeric():
            print("enter number please")
        elif int(number) > max_number:
            print(f"enter number lower than {max_number+1}")
        elif int(number) < min_number:
            print(f"enter number higher than {min_number-1}")
        else:
            print("please enter number")


def draw_game_board(game_board: list[list[int]], is_start: bool = False) -> None:
    """draw_game_board print game board for user

    Arguments:
        game_board {list[list[int]]} -- game board detail
    """
    print("\n" * 40)
    if is_start:
        start_y = random.randint(0, len(game_board) - 1)
        start_x = random.randint(0, len(game_board[0]) - 1)
        game_board[start_y][start_x] = 2
    for y, row in enumerate(game_board):
        for x, cell in enumerate(row):
            print(cell, end="\t")
        print()
