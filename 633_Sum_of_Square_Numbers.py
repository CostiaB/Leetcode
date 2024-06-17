"""
633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Constraints:

    0 <= c <= 231 - 1
"""
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            if (r * r + l * l) == c:
                return True
            if (r * r + l * l) > c:
                r -= 1
                continue
            l += 1
        return False


test0 = {
    'input': {'c': 5

    },
    'output': True
}
test1 = {
    'input': {'c': 3

    },
    'output': False
}


tests = [test0, test1]

for test in tests:
    print(Solution().judgeSquareSum(**test['input']) == test['output'])

"""
Runtime Beats 56.26% O(sqrt(c)
Memory 16.36MB Beats 96.90% 0(1)
"""