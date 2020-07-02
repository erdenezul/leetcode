from collections import Counter
from heapq import heappush, heappop

def frequencySort(s: str) -> str:
    """
    Given a string, sort it
    Link: https://leetcode.com/problems/sort-characters-by-frequency/
    Frequency sort

    .. doctest::
       >>> frequencySort('tree')
       'eetr'
       >>> frequencySort('cccaaa')
       'cccaaa'
       >>> frequencySort('raaeaedere')
       'eeeeaaarrd'
    """
    counter = Counter(s)
    h = []
    for key, value in counter.items():
        heappush(h, (value, key))
    result = ""
    while h:
        row = heappop(h)
        result = row[1] * row[0] + result
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
