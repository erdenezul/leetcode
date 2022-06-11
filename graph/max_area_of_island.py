from typing import List
from collections import deque

class Solution:
    """
    Time complexity: O(n*m), where n is number of rows in given grid, and m is the number
                     of columns.
    Space complexiy: O(n*m), the space used by seen to keep track of visited squares, and the space used
                     by stack.
    Note: if we allowed to modify the grid, we don't have to use seen variable
    .. doctest::
       >>> s= Solution()
       >>> s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
       4
       >>> s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
       6
       >>> s.maxAreaOfIsland([[1,1]])
       2
    """
    def dfs(self, grid: List[List[int]], i:int, j:int, seen:set) -> int:
        size = 0
        n, m = len(grid), len(grid[0])
        stack = deque([(i,j)])
        seen.add((i, j))
        while stack:
            ci, cj = stack.pop()
            size += 1
            for new_i, new_j in ((ci+1, cj),(ci, cj+1), (ci-1, cj), (ci, cj-1)):
                if 0<= new_i < n and 0<=new_j<m and grid[new_i][new_j] and (new_i, new_j) not in seen:
                    stack.append((new_i, new_j))
                    seen.add((new_i, new_j)) 
        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        for i, rows in enumerate(grid):
            for j, _ in enumerate(rows):
                if grid[i][j] == 1 and (i,j) not in seen:
                    size = self.dfs(grid=grid, i=i, j=j, seen=seen)
                    max_area = max(size, max_area)
        return max_area

if __name__ == '__main__':
    import doctest
    doctest.testmod()