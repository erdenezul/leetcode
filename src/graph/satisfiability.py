from typing import List


class Solution:
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
        rank = [1 for _ in range(26)]

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

            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
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
