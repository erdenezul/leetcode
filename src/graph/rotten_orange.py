from collections import deque
from typing import List


class Solution:
    """
    Ref: https://leetcode.com/problems/rotting-oranges/
      Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
      Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    Idea:
        1. Use BFS to calculate rot neighbor oranges every minute
        2. Calculate number of fresh oranges and decrease it every BFS traversal
        3. After all traversal, if there is any fresh oranges which means that
           those oranges does not have neighbor rotten oranges.
    >>> s = Solution()
    >>> s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    4
    >>> s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    -1
    >>> s.orangesRotting([[0,2]])
    0
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh_orange_count = 0
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_orange_count += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        directions = (
            (0, -1),
            (-1, 0),
            (0, 1),
            (1, 0),
        )
        level = fresh_orange_count
        while queue and fresh_orange_count > 0:
            ci, cj, ct = queue.popleft()
            for di, dj in directions:
                if 0 <= di + ci < n and 0 <= dj + cj < m and grid[di + ci][dj + cj] == 1:
                    fresh_orange_count -= 1
                    queue.append((di + ci, dj + cj, ct + 1))
                    grid[di + ci][dj + cj] = 2
                    level = ct + 1
        if fresh_orange_count:
            return -1
        return level


if __name__ == "__main__":
    import doctest

    doctest.testmod()
