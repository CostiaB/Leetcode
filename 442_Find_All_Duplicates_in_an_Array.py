"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears
once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    Each element in nums appears once or twice.
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        cnt = {}
        ans = []
        for i in nums:
            cnt[i] = 1 + cnt.get(i, 0)
            if cnt[i] == 2:
                ans.append(i)

        return ans


test0 = {
    'input': {'nums': [4, 3, 2, 7, 8, 2, 3, 1]

    },
    'output': [2, 3]
}
test1 = {
    'input': {'nums': [1, 1, 2],

    },
    'output': [1]
}
test2 = {
    'input': {'nums': [1],

    },
    'output': []
}

tests = [test0, test1, test2]

for test in tests:
    print(Solution().findDuplicates(**test['input']) == test['output'])

"""
Runtime 262ms Beats 62.65% of users with Python3
Memory 25.25MB Beats 39.33% of users with Python3
"""