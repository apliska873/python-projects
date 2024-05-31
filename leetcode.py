def reverse(self, x: int) -> int:
    x_str = str(x)
    if x < 0:
        is_negative: bool = True
    else:
        is_negative: bool = False
    x_str2: str = ''
    for char in x_str:
        if char == '-':
            continue
        x_str2 = char + x_str2
    try:
        if is_negative:
            x_new: int = int('-' + x_str2)
        else:
            x_new: int = int(x_str2)
    except ValueError:
        return 0
    minimum: int = -(2**31)
    maximum: int = 2**31 - 1
    if x_new > maximum or x_new < minimum:
        return 0
    return x_new


def string_to_integer(s: str) -> int:
    if len(s) == 0:
        return 0
    final_s: str = ""

    for char in s:
        if char.isdigit():
            final_s = char + final_s
        elif char == ' ':
            continue


string_to_integer("5")