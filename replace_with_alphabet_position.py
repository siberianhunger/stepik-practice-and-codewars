def alphabet_position(text):
    """
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.
    """
    str_1, fin_str = text.lower(), ''
    
    for i in str_1:
        if ord(i) >= 97 and ord(i) <= 122:
            fin_str += str(ord(i) - 96) + ' '
    return fin_str[:-1]
