class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Ref: https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
        Complexity: O(n)
        Space: O(1)
        
        >>> s = Solution()
        >>> s.bestClosingTime("YNNY")
        1
        >>> s.bestClosingTime("YYNY")
        2
        """
        # total penalty after closing immediately
        cur_penalty = min_penalty = customers.count('Y')

        earliest_hour = 0
        for i, ch in enumerate(customers):
            # every time we see the customer is not coming we have to increase
            # the penalty otherwise we have to decrease the penalty
            cur_penalty += 1 if ch == 'N' else -1

            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty
        return earliest_hour


if __name__ == "__main__":
    import doctest
    doctest.testmod()