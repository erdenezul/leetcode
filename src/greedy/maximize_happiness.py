from typing import List


class Solution:
    """
    Ref: https://leetcode.com/problems/maximize-happiness-of-selected-children/
    """
    def maximum_happiness_sum(self, happiness: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.maximum_happiness_sum([1,2, 3], 2)
        4
        >>> s.maximum_happiness_sum([1, 1, 1, 1], 2)
        1
        >>> s.maximum_happiness_sum([2, 3, 4, 5], 1)
        5
        """
        happiness.sort(reverse=True)
        answer = pick = 0
        while pick < k:
            answer += max(0, happiness[pick] - pick)
            pick += 1
        return answer

if __name__ == '__main__':
    import doctest
    doctest.testmod()