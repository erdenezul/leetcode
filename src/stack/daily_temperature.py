"""
Topic: Monotonic Decreasing Stack
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        .. doctest::
           >>> s = Solution()
           >>> s.dailyTemperatures([73,74, 75, 71, 69, 72, 76, 73])
           [1, 1, 4, 2, 1, 1, 0, 0]
        """
        res = [0] * len(temperatures)
        stack = []  # pair [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([temp, index])
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
