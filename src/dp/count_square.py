from typing import List

class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
        15
        >>> s.countSquares([[1,0,1],[1,1,0],[1,1,0]])
        7
        """
        square_count = 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = matrix[i][0]
            square_count += dp[i][0]

        for j in range(1,m):
            dp[0][j] = matrix[0][j]
            square_count += dp[0][j]
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                square_count += dp[i][j]
        print(dp)
        return square_count

if __name__ == '__main__':
    import doctest
    doctest.testmod()