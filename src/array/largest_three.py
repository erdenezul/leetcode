class Solution:
    """
    >>> s = Solution()
    >>> s.largestGoodInteger("6777133339")
    '777'
    >>> s.largestGoodInteger("2300019")
    '000'
    >>> s.largestGoodInteger("42352338")
    ''
    """
    def largestGoodInteger(self, num: str) -> str:
        values = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        for val in values:
            if val in num:
                return val
        return ""

if __name__ == "__main__":
    import doctest
    doctest.testmod()