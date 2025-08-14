from typing import List

class Solution:
    """
    https://leetcode.com/problems/pascals-triangle/
    >>> s = Solution()
    >>> s.generate(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> s.generate(1)
    [[1]]
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows + 1):
            res.append([1] + [res[-1][j] + res[-1][j + 1] for j in range(i - 2)] + [1])
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()