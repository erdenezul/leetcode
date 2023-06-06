from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        >>> s = Solution()
        >>> s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        4
        >>> s.maximalSquare([["0","1"],["1","0"]])
        1
        >>> s.maximalSquare([["0"]])
        0
        """
        max_side = 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            max_side = max(max_side, dp[i][0])

        for j in range(1, m):
            dp[0][j] = int(matrix[0][j])
            max_side = max(max_side, dp[0][j])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == "__main__":
    import doctest

    doctest.testmod()
