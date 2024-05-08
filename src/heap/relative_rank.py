from typing import List
from heapq import heappop, heappush

class Solution:
    def relativeRanks(self, score: List[int]) -> List[str]:
        """
        Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
        who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

        Basic idea is that we can use a max heap to store the scores and their corresponding index.
        Then we can pop the heap and assign the rank to the corresponding index.
        >>> s = Solution()
        >>> s.relativeRanks([5, 4, 3, 2, 1])
        ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        >>> s.relativeRanks([10, 3, 8, 9, 4])
        ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
        """
        heap = []
        for i, s in enumerate(score):
            heappush(heap, (-s, i))
        result = [0] * len(score)
        rank_map = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal'
        }
        for i in range(len(score)):
            s, index = heappop(heap)
            result[index] = rank_map.get(i + 1, str(i + 1))

        return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()