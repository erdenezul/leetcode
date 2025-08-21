from typing import List

class Solution:
    """
    https://leetcode.com/problems/count-submatrices-with-all-ones/
    >>> s = Solution()
    >>> s.numSubmat([[1,0,1],[1,1,0],[1,1,0]])
    13
    >>> s.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])
    24
    """
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        height = [0] * n

        for _, rows in enumerate(mat):
            # Calculate heights for the current row
            for j, val in enumerate(rows):
                height[j] += height[j] + 1 if val == 1 else 0
            
            # Use monotonic stack to count rectangles for this row
            sub_res = [0] * n
            stack = [-1]
            for j in range(n):
                while stack[-1] != -1 and height[stack[-1]] >= height[j]:
                    stack.pop()
                k = stack[-1]
                # Formula: new rectangles + extended old ones
                sub_res[j] = height[j] * (j - k)
                if k != -1:
                    sub_res[j] += sub_res[k]
                stack.append(j)
            res += sum(sub_res)

        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()