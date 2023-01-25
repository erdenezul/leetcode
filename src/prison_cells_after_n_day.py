def transform_cells(cells):
    """
    Transform cells based on rules

    >>> transform_cells([0, 1, 0, 1, 1, 0, 0, 1])
    [0, 1, 1, 0, 0, 0, 0, 0]
    >>> transform_cells([0, 1, 1, 0, 0, 0, 0, 0])
    [0, 0, 0, 0, 1, 1, 1, 0]
    """
    res = [0] * 8
    for i in range(1, 7):
        res[i] = int(cells[i - 1] == cells[i + 1])
    return res


def prison_after_n_days(cells, n):
    """
    Returns cells occupancy after n days

    >>> prison_after_n_days([0, 1, 0, 1, 1, 0, 0, 1], 7)
    [0, 0, 1, 1, 0, 0, 0, 0]
    >>> prison_after_n_days([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
    [0, 0, 1, 1, 1, 1, 1, 0]
    >>> prison_after_n_days([1,1,0,0,0,0,1,1], 7)
    [0, 0, 1, 1, 1, 1, 0, 0]
    >>> prison_after_n_days([0 ,0, 1, 1, 1, 1, 0, 0], 8)
    [0, 0, 0, 1, 1, 0, 0, 0]
    """
    mapping = {}
    for i in range(n):
        s = "".join(map(str, cells))
        if s in mapping:
            loop_len = i - mapping[s]
            return prison_after_n_days(cells, (n - i) % loop_len)
        else:
            mapping[s] = i
            cells = transform_cells(cells)
    return cells


if __name__ == "__main__":
    import doctest

    doctest.testmod()
