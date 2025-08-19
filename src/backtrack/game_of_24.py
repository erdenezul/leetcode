from typing import List

class Solution:
    """
    https://leetcode.com/problems/24-game/
    >>> s = Solution()
    >>> s.judgePoint24([4,1,8,7])
    True
    >>> s.judgePoint24([1,2,1,2])
    False
    """
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        
        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            # Try every unordered pair (i, j), i < j
            n = len(nums)
            for i, a in enumerate(nums):
                for j, b in enumerate(nums):
                    if i >= j: continue
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]

                    # Generate possible results from a and b
                    candidates = [
                        a + b,
                        a - b,
                        b - a,
                        a * b,
                    ]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    # Prune duplicates: for + and * (commutative ops), avoid trying both orders
                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])


if __name__ == "__main__":
    import doctest
    doctest.testmod()