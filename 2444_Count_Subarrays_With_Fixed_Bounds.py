"""
2444. Count Subarrays With Fixed Bounds
You are given an integer array nums and two integers minK and maxK.
A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:

    2 <= nums.length <= 105
    1 <= nums[i], minK, maxK <= 106
"""


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        minA = -1
        maxA = -1
        bad = -1
        ans = 0
        l = 0
        for i, el in enumerate(nums):
            if not minK <= el <= maxK:
                bad = i
            if el == maxK:
                maxA = i
            if el == minK:
                minA = i
            start = min(minA, maxA)
            if start > bad:
                ans += start - bad
        return ans


test0 = {
    'input': {'nums': [1, 3, 5, 2, 7, 5],
              'minK': 1,
              'maxK': 5

    },
    'output': 2
}
test1 = {
    'input': {'nums': [1, 1, 1, 1],
              'minK': 1,
              'maxK': 1

              },
    'output': 10
}


tests = [test0, test1]

for test in tests:
    print(Solution().countSubarrays(**test['input']) == test['output'])

"""
Runtime 683ms Beats 81.27% of users with Python3
Memory 31.13MB Beats 17.63% of users with Python3
"""