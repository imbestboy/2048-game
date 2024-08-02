import functions

x = functions.get_number(
    input_text="enter game width (3 - 7) : ", max_number=7, min_number=3
)
y = functions.get_number(
    input_text="enter game height (3 - 7) : ", max_number=7, min_number=3
)
game_board = [[0 for _ in range(x)] for _ in range(y)]

DIRECTIONS = {"w": "up", "s": "down", "a": "left", "d": "right"}

while functions.draw_game_board(game_board=game_board):
    movement = input("enter one of w a s d : ").lower()
    if movement not in ("w", "a", "s", "d"):
        print("\n" * 40)
        functions.draw_game_board(game_board=game_board)
        print("please enter one of w s a d !")
        continue

    game_board = functions.move_numbers(
        game_board=game_board, direction=DIRECTIONS[movement]
    )

print("\n" * 40)

print("GAME OVER")
input("press enter to continue")
