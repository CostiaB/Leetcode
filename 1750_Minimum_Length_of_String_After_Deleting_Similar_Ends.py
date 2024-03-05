"""
1750. Minimum Length of String After Deleting Similar Ends
Solved
Medium
Topics
Companies
Hint

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the
string any number of times:

    Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero times).



Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Example 4:

Input: s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
Output: 1

Constraints:

    1 <= s.length <= 105
    s only consists of characters 'a', 'b', and 'c'.


"""


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        current = 0
        while l < r and s[l] == s[r]:
            current = s[l]
            while l <= r and s[l] == current:
                l += 1
            while l <= r and s[r] == current:
                r -= 1
        return r - l + 1

test0 = {
    'input': {
        's': "ca"
    },
    'output': 2
}
test1 = {
    'input': {
        's': "cabaabac"
    },
    'output': 0
}
test2 = {
    'input': {
        's': "aabccabba"
    },
    'output': 3
}
test3 = {
    'input': {
        's': "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
    },
    'output': 1
}

tests = [test0, test1, test2, test3]
for test in tests:
    print(Solution().minimumLength(**test['input']) == test['output'])

"""
Runtime 66ms Beats73.46% of users with Python3
Memory 17.40MB Beats75.83% of users with Python3
"""