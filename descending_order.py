def descending_order(num: int) -> int:
    """
    Your task is to make a function that can take any non-negative integer as an argument and return it
    with its digits in descending order.
    Essentially, rearrange the digits to create the highest possible number.
    """
    return int(''.join(sorted([x for x in str(num)], reverse=True)))