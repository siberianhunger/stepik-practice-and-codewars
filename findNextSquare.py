def find_next_square(sq: int) -> int:
    """
    Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
    Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
    If the parameter is itself not a perfect square then -1 should be returned.
    You may assume the parameter is non-negative.
    :return:
    """
    initial_num = pow(sq, 0.5)
    if initial_num % 1 == 0:
        return (initial_num + 1)**2
    else:
        return -1
