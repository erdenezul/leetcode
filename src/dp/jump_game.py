from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.canJump([2,3,1,1,4])
        True
        >>> s.canJump([3,2,1,0,4])
        False
        """
        reachable = 0

        for i, num in enumerate(nums):
            if (reachable < i):
                return False
            reachable = max(reachable, i + num)
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()