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


def draw_game_board(game_board: list[list[int]]) -> bool:
    """draw_game_board print game board for user

    Arguments:
        game_board {list[list[int]]} -- game board detail

    Returns:
        bool -- user can continue playing or not
    """
    print("\n" * 40)
    print("HELP :")
    print("up => w")
    print("left => a")
    print("down => s")
    print("right => d")
    y_count = len(game_board)
    x_count = len(game_board[0])
    locations = [(y, x) for y in range(y_count) for x in range(x_count)]
    while True:
        if not locations:
            return False
        y, x = random.choice(locations)
        if game_board[y][x] == 0:
            game_board[y][x] = 2
            break
        locations.remove((y, x))
    for y, row in enumerate(game_board):
        for x, cell in enumerate(row):
            print(cell, end="\t")
        print()
    return True


def move_numbers(game_board: list[list[int]], direction: str) -> list[list[int]]:
    for _ in range(len(game_board)):
        if direction == "up":
            for y, row in enumerate(game_board):
                for x, cell in enumerate(row):
                    if y != 0 and cell != 0:
                        if game_board[y - 1][x] == 0:
                            game_board[y][x] = 0
                            game_board[y - 1][x] = cell
                        elif game_board[y - 1][x] == cell:
                            game_board[y][x] = 0
                            game_board[y - 1][x] = cell * 2
        elif direction == "down":
            for y, row in enumerate(game_board):
                for x, cell in enumerate(row):
                    if y != len(game_board) - 1 and cell != 0:
                        if game_board[y + 1][x] == 0:
                            game_board[y][x] = 0
                            game_board[y + 1][x] = cell
                        elif game_board[y + 1][x] == cell:
                            game_board[y][x] = 0
                            game_board[y + 1][x] = cell * 2
    for _ in range(len(game_board[0])):
        if direction == "left":
            for y, row in enumerate(game_board):
                for x, cell in enumerate(row):
                    if x != 0 and cell != 0:
                        if game_board[y][x - 1] == 0:
                            game_board[y][x] = 0
                            game_board[y][x - 1] = cell
                        elif game_board[y][x - 1] == cell:
                            game_board[y][x] = 0
                            game_board[y][x - 1] = cell * 2
        elif direction == "right":
            for y, row in enumerate(game_board):
                for x, cell in enumerate(row):
                    if x != len(game_board[0]) - 1 and cell != 0:
                        if game_board[y][x + 1] == 0:
                            game_board[y][x] = 0
                            game_board[y][x + 1] = cell
                        elif game_board[y][x + 1] == cell:
                            game_board[y][x] = 0
                            game_board[y][x + 1] = cell * 2
    return game_board
