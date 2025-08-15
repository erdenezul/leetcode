class Solution:
    """
    >>> s = Solution()
    >>> s.isPowerOfFour(16)
    True
    >>> s.isPowerOfFour(1)
    True
    >>> s.isPowerOfFour(0)
    False
    >>> s.isPowerOfFour(-2147483648)
    False
    """
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 !=0:
                return False
            n = n // 4
        return True

 
if __name__ == "__main__":
    import doctest
    doctest.testmod()