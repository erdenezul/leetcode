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

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.seen = set()
        enclaves = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in self.seen:
                    enclaves += self.bfs((i, j))
        return enclaves

    def bfs(self, cell):
        self.seen.add(cell)
        queue = [cell]
        enclaves = 0
        walkable = False
        while queue:
            r, c = queue.pop(0)
            if r == 0 or r == len(self.grid) - 1 or c == 0 or c == len(self.grid[0]) - 1:
                walkable = True
            else:
                enclaves += 1
            if r < len(self.grid) - 1 and self.grid[r + 1][c] == 1 and (r + 1, c) not in self.seen:
                self.seen.add((r + 1, c))
                queue.append((r + 1, c))
            if r > 0 and self.grid[r - 1][c] == 1 and (r - 1, c) not in self.seen:
                self.seen.add((r - 1, c))
                queue.append((r - 1, c))
            if c < len(self.grid[r]) - 1 and self.grid[r][c + 1] == 1 and (r, c + 1) not in self.seen:
                self.seen.add((r, c + 1))
                queue.append((r, c + 1))
            if c > 0 and self.grid[r][c - 1] == 1 and (r, c - 1) not in self.seen:
                self.seen.add((r, c - 1))
                queue.append((r, c - 1))
        return enclaves if not walkable else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
