from operator import truediv
from typing import List

class Solution:
    """
    1. We need traversal -> DFS would be fine
    2. DFS traversal should check additional constraint
       if zero is reached 
    >>> s= Solution()
    >>> s.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
    2
    >>> s.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])
    1
    """
    def isClosedIsland(self, grid: List[List[int]], i:int, j: int, n: int, m: int) -> bool:
        if grid[i][j] == -1 or grid[i][j] == 1: 
            return True
        if self.isOnPerimeter(i=i, j=j, n=n,m=m):
            return False
        grid[i][j] = -1
        left = self.isClosedIsland(grid, i-1, j, n, m)
        right = self.isClosedIsland(grid, i+ 1, j, n, m)
        down = self.isClosedIsland(grid, i, j+1, n, m)
        up = self.isClosedIsland(grid, i, j-1,n,m )
        return left and right and down and up

    def isOnPerimeter(self, i: int, j: int, n: int, m: int) -> bool:
        return i == 0 or j==0 or i == n-1 or j == m-1

    def closedIsland(self, grid: List[List[int]]) -> int:
        num_island = 0
        n,m = len(grid), len(grid[0])
        for i in range(1, n-1):
            for j in range(1,m-1):
                if grid[i][j] == 0:
                    if self.isClosedIsland(grid, i, j, n, m):
                        num_island += 1
        return num_island

if __name__ == '__main__':
    import doctest
    doctest.testmod()