"""
2370. Longest Ideal Subsequence

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following
conditions are satisfied:

    t is a subsequence of the string s.
    The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing
the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a'
and 'z' is 25, not 1.

Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

Constraints:

    1 <= s.length <= 105
    0 <= k <= 25
    s consists of lowercase English letters.
"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        ans = 0
        for c in s:
            curr = ord(c) - ord("a") # 0 to 25
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = max(dp[curr], longest)

        return max(dp)


test0 = {
    'input': {'k': 2,
              's': "acfgbd"
    },
    'output': 4
}

test1 = {
    'input': {'k': 3,
              's': "abcd"
    },
    'output': 4
}
test2 = {
    'input': {'k': 2,
              's': "pvjcci"
    },
    'output': 2
}

tests = [test0, test1, test2]

for test in tests:
    print(Solution().longestIdealString(**test['input']) == test['output'])

"""
Runtime 1602ms Beats 34.31% of users with Python3
Memory 17.28MB Beats 93.43% of users with Python3
"""