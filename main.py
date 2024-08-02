import functions

x = functions.get_number(
    input_text="enter game width (3 - 7) : ", max_number=7, min_number=3
)
y = functions.get_number(
    input_text="enter game height (3 - 7) : ", max_number=7, min_number=3
)
game_board = [[0 for _ in range(x)] for _ in range(y)]
