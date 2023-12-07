from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.mctFromLeafValues([6,2,4])
        32
        >>> s.mctFromLeafValues([4,11])
        44
        >>> s.mctFromLeafValues([15,13,5,3,15])
        500
        """
        n = len(arr)
        memory = [[(-1, -1) for _ in range(n + 1)] for _ in range(n + 1)]
        return self.dp(0, n - 1, arr, memory)[1]

    # [6,2, 4]
    def dp(self, start: int, end: int, values: List[int], mem):
        """
        Returns two pair of values (max_of_child, sum up until this root)
        [6,2] -> [6], [2]
            [6] -> (6, 0)
            [2] -> (2, 0)
            [6, 2] -> (6, 12)

        """
        if mem[start][end][0] != -1:
            return mem[start][end]
        if start == end:
            mem[start][end] = (values[start], 0)
            return mem[start][end]

        nonLeafSum = float("inf")
        maxLeaf = float("-inf")
        for i in range(start, end):
            left = self.dp(start, i, values, mem)
            right = self.dp(i + 1, end, values, mem)
            maxLeaf = max(left[0], right[0], maxLeaf)
            nonLeafSum = min(nonLeafSum, left[0] * right[0] + left[1] + right[1])
        mem[start][end] = (maxLeaf, nonLeafSum)
        return mem[start][end]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
