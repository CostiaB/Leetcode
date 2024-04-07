"""
678. Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax +1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax +1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = ( * ) (
                leftMin = 0
        return leftMin == 0


test0 = {
    'input': {'s': "()"

    },
    'output': True
}
test1 = {
    'input': {'s': "(*)"

    },
    'output': True
}
test2= {
    'input': {'s': "(*))"

    },
    'output': True
}

tests = [test0, test1, test2]

for test in tests:
    print(Solution().checkValidString(**test['input']) == test['output'])


"""
Runtime 33ms Beats 74.42% of users with Python3
Memory 16.56MB Beats 50.32% of users with Python3
"""
