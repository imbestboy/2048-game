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
        elif int(number) > max_number:
            print(f"enter number lower than {max_number+1}")
        elif int(number) < min_number:
            print(f"enter number higher than {min_number-1}")
        else:
            print("please enter number")
