# 279. Perfect Squares

'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



Constraints:

    1 <= n <= 104


'''

import math


class Solution:
    @staticmethod
    def numSquares(n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]


## test 1. n = 12
# expected ans = 3
ans = Solution.numSquares(n=12)
print(ans)

## test 2. n = 13
# expected ans = 2

ans = Solution().numSquares(n=13)
print(ans)


'''
Runtime 2313ms Beats 64.34%of users with Python3
Memory 16.68MB Beats 81.54%of users with Python3
'''