# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def giveMeLetter(a, b):
    if a == "?" and b == "?":
        return "a"
    if a == "":
        a = b
    value = ord(a)
    value -= 1
    if value == ord(b):
        value -= 1
    # a -> 95, 96
    # b -> 96, 96
    if value == 95 or value == 96:
        value += 10  # just random value

    return chr(value)


def solution(riddle):
    n = len(riddle)
    result = ""
    for i in range(n):
        if riddle[i] != "?":
            result += riddle[i]
            continue
        # sufficient condition would be replace any letter except neighbors
        # avoid index out of range in first letter ?
        left = riddle[i + 1] if len(result) == 0 else result[-1]
        right = riddle[i + 1] if i + 1 < n else result[-1]
        letter = giveMeLetter(left, right)
        result += letter
    return result
