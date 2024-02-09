"""
368. Largest Divisible Subset
Solved
Medium
Topics
Companies

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
"""


class Solution:


    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        self.l = len(nums)
        self.res = []
        self.memory = [-1] * len(nums)
        self.searcher(nums, 0, [], 1)
        return self.res

    def searcher(self, nums, index, curr, prev):
        if len(curr) > len(self.res):
            self.res = curr[:]

        for i in range(index, self.l):
            if len(curr) > self.memory[i] and nums[i] % prev == 0:
                self.memory[i] = len(curr)
                curr.append(nums[i])
                self.searcher(nums, i + 1, curr, nums[i])
                curr.pop()


"""
Runtime  311ms Beats 33.10%of users with Python3
Memory 16.67MB Beats 96.03%of users with Python3
"""
#test 1  [1,2,3] ans = [1,2]

ans = Solution().largestDivisibleSubset([1, 2, 3])
print(ans)
#test 2 [1,2,4,8] ans = [1,2,4,8]
ans = Solution().largestDivisibleSubset([1, 2, 4, 8])
print(ans)
