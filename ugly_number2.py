def nth_ugly_number(n):
    """
    Return nth ugly number
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first
                 10 ugly numbers

    >>> nth_ugly_number(10)
    12
    """
    if n == 0:
        return 0
    i, j, k = 0, 0, 0
    numbers = [1]
    while len(numbers) < n:
        t1 = numbers[i] * 2
        t2 = numbers[j] * 3
        t3 = numbers[k] * 5
        min_those = min(t1, t2, t3)
        numbers.append(min_those)
        if min_those == t1:
            i += 1
        if min_those == t2:
            j += 1
        if min_those == t3:
            k += 1
    return numbers[n - 1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
