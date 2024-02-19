"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: n = 3
Output: false



Constraints:

    -231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        #(n & (n - 1)) == 0: This part checks if n and n - 1 have any common bits.
        # If n is a power of 2, it will have only one bit 1 (the most significant bit).
        # When you subtract 1 from it, all bits to the right of that bit become 1.
        # Therefore, the bitwise AND operation n & (n - 1) will be 0 only if n has only one bit set
        # (i.e., it is a power of 2).

# case 1 n = 1 ans True
ans = Solution().isPowerOfTwo(1)
print(ans)
# case 2 n = 16 ans True
ans = Solution().isPowerOfTwo(16)
print(ans)
# case 3 n = 3 ans False
ans = Solution().isPowerOfTwo(3)
print(ans)

"""
Runtime 32ms Beats82.72% of users with Python3
Memory 16.66MB Beats53.28% of users with Python3
"""