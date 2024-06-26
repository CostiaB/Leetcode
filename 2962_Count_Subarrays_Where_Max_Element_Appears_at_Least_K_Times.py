"""
2962. Count Subarrays Where Max Element Appears at Least K Times
Solved
Medium
Topics
Companies

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3],
 [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 106
    1 <= k <= 105
"""

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        m = max(nums)
        cnt = 0
        l = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == m:
                cnt += 1
            while cnt == k:
                if nums[l] == m:
                    cnt -= 1
                l += 1
            ans += l

        return ans


test0 = {
    'input': {'nums': [1, 3, 2, 3, 3],
              'k': 2

    },
    'output': 6
}
test1 = {
    'input': {'nums': [1, 4, 2, 1],
              'k': 3

    },
    'output': 0
}


tests = [test0, test1]

for test in tests:
    print(Solution().countSubarrays(**test['input']) == test['output'])

"""
Runtime 838ms Beats 95.04% of users with Python3
Memory 30.73MB Beats 97.33% of users with Python3
"""