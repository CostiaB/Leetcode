"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(reverse=True)
        ans = ""
        f = strs[0]
        l = strs[-1]
        for a in range(min(len(f), len(l))):
            if f[a] != l[a]:
                return ans
            ans += f[a]

        return ans

test0 = {
    'input': {'strs': ["flower", "flow", "flight"]

    },
    'output': "fl"
}
test1 = {
    'input': {'strs': ["dog", "racecar", "car"],

    },
    'output': ""
}

tests = [test0, test1]

for test in tests:
    print(Solution().longestCommonPrefix(**test['input']) == test['output'])

"""
Runtime 39ms Beats 49.99% of users with Python3
Memory 16.62MB Beats 47.01% of users with Python3
"""