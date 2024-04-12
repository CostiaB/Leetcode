"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:

    1 <= k <= num.length <= 105
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # stack for keeping track of the digits
        stack = []
        for digit in num:
            # Pop digits from the stack until the top digit
            while k > 0 and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            # append current digit to the stack
            stack.append(digit)

        stack = stack[:len(stack) - k]
        # join digits and remove leading zeroes
        ans = ''.join(stack).lstrip("0")
        return ans if ans else "0"


test0 = {
    'input': {'num': "1432219",
              'k': 3

    },
    'output': "1219"
}
test1 = {
    'input': {'num': "10200",
              'k': 1

    },
    'output': "200"
}
test2 = {
    'input': {'num': "10",
              'k': 2

    },
    'output': "0"
}


tests = [test0, test1, test2]

for test in tests:
    print(Solution().removeKdigits(**test['input']) == test['output'])

"""
Runtime 56ms Beats 67.25% of users with Python3
Memory 17.89MB Beats 92.26% of users with Python3
"""