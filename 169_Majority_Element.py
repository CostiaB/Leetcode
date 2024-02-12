"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        tmp = {}
        res = freq = 0

        for n in nums:
            tmp[n] = 1 + tmp.get(n, 0)
            if tmp[n] > freq:
                res = n
                freq = tmp[n]

        return res


"""
Runtime 152ms Beats 18.71% of users with Python3
Memory 18.03MB Beats 63.51% of users with Python3
"""

# test  case 1 nums = [3, 2, 3] ans = 3
ans = Solution().majorityElement([3, 2, 3])
print(ans)

# test  case 2 nums =[2, 2, 1, 1, 1, 2, 2]  ans = 2

ans = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
print(ans)