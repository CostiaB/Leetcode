"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1



Constraints:

    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n

"""

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        delta = {}
        for rel in trust:
            delta[rel[1]] = delta.get(rel[1], 0) + 1
            delta[rel[0]] = delta.get(rel[0], 0) - 1
        for i in range(1, n+1):
            if delta.get(i, 0) == n - 1:
                return i
        return -1


test0 = {
    "input": {
        "n": 2,
        "trust": [[1,2]]
    },
    "output": 2
}

test1 = {
    "input": {
        "n": 3,
        "trust": [[1,3],[2,3]]
    },
    "output": 3
}

test2 = {
    "input": {
        "n": 3,
        "trust": [[1,3],[2,3],[3,1]]
    },
    "output": -1
}

tests = [test0, test1, test2]

for test in tests:
    output = Solution().findJudge(**test["input"])
    print(output, test["output"] == output)

"""
Runtime 589ms Beats91.22% of users with Python3
Memory 21.48MB Beats95.97% of users with Python3
"""