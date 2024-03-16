"""
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal
number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sums = {}  # count[1] -  count[0] -> index
        zeroes = 0
        ones = 0
        ans = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeroes += 1
            else:
                ones += 1
            if ones - zeroes not in sums:
                sums[ones - zeroes] = i

            if ones == zeroes:
                ans = ones + zeroes
            else:
                idx = sums[ones - zeroes]
                ans = max(ans, i - idx)

        return ans


test0 = {
    'input': {'nums': [0, 1]

    },
    'output': 2
}
test1 = {
    'input': {'nums': [0, 1, 0],

    },
    'output': 2
}

tests = [test0, test1]

for test in tests:
    print(Solution().findMaxLength(**test['input']) == test['output'])

"""
Runtime 628ms Beats 37.99% of users with Python3
Memory 22.05MB Beats 91.38% of users with Python3
"""