from typing import List
from collections import deque


class Solution:
    """
    .. doctest::
       >>> s = Solution()
       >>> #s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
       #3
       >>> #s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
       #0
       >>> #s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])
       #3
       >>> #s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])
       #3
       >>> s.numEnclaves([[0,0,0,1,1,1,0,1,1,1,1,1,0,0,0],[1,1,1,1,0,0,0,1,1,0,0,0,1,1,1],[1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],[1,1,0,1,0,1,1,0,0,0,1,1,0,1,0],[1,1,1,1,0,0,0,1,1,1,0,0,0,1,1],[1,0,1,1,0,0,1,1,1,1,1,1,0,0,0],[0,1,0,0,1,1,1,1,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,1,1,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,0,0,0,0,1,0,1],[1,1,1,0,1,0,1,0,1,1,1,0,0,1,0]])
       27
    """

    def valid(self, grid: List[List[int]], i: int, j: int) -> bool:
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1

    def dfsUtil(self, grid: List[List[int]], i: int, j: int) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        stack = [(i, j)]
        while stack:
            ci, cj = stack.pop()
            grid[ci][cj] = 0
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if self.valid(grid, ni, nj):
                    stack.append((ni, nj))

    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        # walk on rows
        for i in range(n):
            self.dfsUtil(grid, i, 0)
            self.dfsUtil(grid, i, m - 1)
        # walk on column boundary
        for j in range(m):
            self.dfsUtil(grid, 0, j)
            self.dfsUtil(grid, n - 1, j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count += 1

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
