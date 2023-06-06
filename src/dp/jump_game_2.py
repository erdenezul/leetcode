from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.jump([2,3,1,1,4])
        2
        >>> s.jump([2,3,0,1,4])
        2
        """
        res = 0
        l = r = 0
        # 0,0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
