"""
238. Product of Array Except Self
Medium
Topics
Companies

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.



Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for
space complexity analysis.)

"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [1] * length
        right, left = 1, 1
        for i in range(length):
            ans[i] *= left
            left = left * nums[i]
            ans[length - i - 1] *= right
            right = right * nums[length - i - 1]
        return ans

test0 = {
    'input': {'nums': [1, 2, 3, 4],

    },
    'output': [24, 12, 8, 6]
}
test1 = {
    'input': {'nums': [-1, 1, 0, -3, 3],

    },
    'output': [0,0,9,0,0]
}

tests = [test0, test1]

for test in tests:
    print(Solution().productExceptSelf(**test['input']) == test['output'])

"""
Runtime 167ms Beats 56.17% of users with Python3
Memory 23.79MB Beats78.87% of users with Python3
"""