
def island_perimeter(grid):
    """
    >>> island_perimeter([
    ...     [0, 1, 0, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 1, 0, 0],
    ...     [1, 1, 0, 0],])
    16
    """
    m, n, perimeter = len(grid), len(grid[0]), 0
    for i in range(m):
        for j in range(n):
            perimeter += 4 *grid[i][j]
            if i > 0: perimeter -= grid[i][j] * grid[i-1][j]
            if i < m -1: perimeter -= grid[i][j] * grid[i + 1][j]
            if j > 0: perimeter -= grid[i][j] * grid[i][j - 1]
            if j < n - 1: perimeter -= grid[i][j] *grid[i][j + 1]
    return perimeter
if __name__ == '__main__':
    import doctest
    doctest.testmod()
