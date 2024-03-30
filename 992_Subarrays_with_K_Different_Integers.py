"""
992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

    1 <= nums.length <= 2 * 104
    1 <= nums[i], k <= nums.length


"""
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        l_start = 0
        l_finish = 0
        ans = 0

        for r in range(len(nums)):
            cnt[nums[r]] += 1

            while len(cnt) > k:
                cnt[nums[l_start]] -= 1
                if cnt[nums[l_start]] == 0:
                    cnt.pop(nums[l_start])
                l_start += 1
                l_finish = l_start

            while cnt[nums[l_start]] > 1:
                cnt[nums[l_start]] -= 1
                l_start += 1

            if len(cnt) == k:
                ans += l_start - l_finish + 1
        return ans


test0 = {
    'input': {'nums': [1, 2, 1, 2, 3],
              'k': 2

    },
    'output': 7
}
test1 = {
    'input': {'nums': [1, 2, 1, 3, 4],
              'k': 3

    },
    'output': 3
}


tests = [test0, test1]

for test in tests:
    print(Solution().subarraysWithKDistinct(**test['input']) == test['output'])


"""
Runtime 306ms Beats 89.47% of users with Python3
Memory 19.72MB Beats 85.33% of users with Python3
"""