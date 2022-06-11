from typing import List

class Solution:
    """
    .. doctest::
       >>> s = Solution()
       >>> s.numIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
       1
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            if i+1<n:
                dfs(i+1, j)
            if j+1<m:
                dfs(i, j+1)
            if i > 0:
                dfs(i-1, j)
            if j > 0:
                dfs(i, j-1)
        for i, rows in enumerate(grid):
            for j, col in enumerate(rows):
                if col == '1':
                    dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
  import doctest
  doctest.testmod()