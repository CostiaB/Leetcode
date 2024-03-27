"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous
subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = 0
        l = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            ans += (r - l + 1)

        return ans


test0 = {
    'input': {'nums': [10, 5, 2, 6],
              "k": 100

              },
    'output': 8
}
test1 = {
    'input': {'nums': [1, 2, 3],
              'k': 0

              },
    'output': 0
}

tests = [test0, test1]

for test in tests:
    print(Solution().numSubarrayProductLessThanK(**test['input']) == test['output'])

'''
Runtime 517ms Beats 29.03% of users with Python3
Memory 18.99MB Beats 98.91% of users with Python3
'''