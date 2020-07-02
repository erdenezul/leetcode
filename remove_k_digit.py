def remove_k_digits(num: str, k: int) -> str:
    """
    Remove k digits from num which minimizes new number.

    .. doctest::
       >>> remove_k_digits("1432219", 3)
       '1219'
       >>> remove_k_digits("10200", 1)
       '200'
       >>> remove_k_digits("10", 2)
       '0'
       >>> remove_k_digits("1173", 2)
       '11'
    """
    n = len(num)
    if n == k:
        return "0"
    stack = []
    nk = k
    for c in num:
        while nk and stack and stack[-1] > c:
            stack.pop()
            nk -= 1
        stack.append(c)

    answer = "".join(stack[0 : n - k]).lstrip("0")
    if answer:
        return answer
    else:
        return "0"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
