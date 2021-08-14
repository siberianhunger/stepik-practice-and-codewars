def square_digits(num: int) -> int:
    """You are asked to square every digit of a number and concatenate them.
    For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

    :arg num - number given to square every digit of it.
    """
    s = ''
    while num:
        s = str((num % 10) * (num % 10)) + s
        num //= 10
    if s:
        return int(s)
    else:
        return 0
