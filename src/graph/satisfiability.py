from typing import List


class Solution:
    """
    Approach
    Disjoint set
    1. We will store variables in same component if they are equal
    2. Then we will check non-equality equtions, if both variables in any of those equation are in same component, we return false.

    Idea:
        1. Traverse all edges with == to group them as cluster
        2. Traverse all edges with != to check if there is any collission
    """

    def equationsPossible(self, equations: List[str]) -> bool:
        """
        >>> s = Solution()
        >>> s.equationsPossible(["a==b","b!=a"])
        False
        >>> s.equationsPossible(["b==a","a==b"])
        True
        >>> s.equationsPossible(["a==b","b==c","c==d","d!=a"])
        False
        >>> s.equationsPossible(["a==b","b!=c","c==a"])
        False
        >>> s.equationsPossible(["a!=b","b!=c","c!=a"])
        True
        """
        parent = [i for i in range(26)]

        def find(n: str):
            p = parent[ord(n) - 97]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a: str, b: str):
            pa, pb = find(a), find(b)

            if pa == pb:
                return False

            parent[pb] = pa
            return True

        for equation in equations:
            if equation[1] == "=":
                union(equation[0], equation[3])

        for equation in equations:
            a, b = equation[0], equation[3]
            if equation[1] == "!" and find(a) == find(b):
                return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
