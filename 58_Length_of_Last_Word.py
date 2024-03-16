"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.


"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        l = len(s) - 1
        while l >= 0:
            if s[l] == " " and ans == 0:
                l -= 1
                continue
            elif s[l] == ' ' and ans > 0:
                return ans
            ans += 1
            l -= 1
        return ans

test0 = {
    'input': {'s': "Hello World"
    },
    'output': 5
}
test1 = {
    'input': {'s': "   fly me   to   the moon  "
    },
    'output': 4
}
test2 = {
    'input': {'s': "luffy is still joyboy"
    },
    'output': 6
}
test3 = {
    'input': {'s': "a"
    },
    'output': 1
}

tests = [test0, test1, test2, test3]

for test in tests:
    print(Solution().lengthOfLastWord(**test['input']) == test['output'])

"""
Runtime 26ms Beats96.05% of users with Python3
Memory 16.55MB Beats83.79% of users with Python3
"""