from typing import List


def likes(array: List) -> str:
    result = ""
    length = len(array)
    if length == 0:
        result = "no one likes this"
    elif length == 1:
        result = f"{array[0]} likes this"
    elif length == 2:
        result = f"{array[0]} and {array[1]} like this"
    elif length == 3:
        result = f"{array[0]}, {array[1]} and {array[2]} like this"
    elif length > 3:
        result = f"{array[0]}, {array[1]} and {length-2} others like this"
    return result
