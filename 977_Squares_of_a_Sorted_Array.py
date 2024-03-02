"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
test0={
    'input':[-4,-1,0,3,10],
    'output':[0,1,9,16,100]
}
test1={
    'input':[-7,-3,2,3,11],
    'output':[4,9,9,49,121]
}
tests = [test0, test1]

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        ans = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans.append(nums[l]**2)
                l += 1
            else:
                ans.append(nums[r]**2)
                r -= 1
        return ans[::-1]


for test in tests:
    print(Solution().sortedSquares(test['input']) == test['output'])

"""
Runtime 155ms Beats64.40% of users with Python3
Memory 18.90MB Beats55.74% of users with Python3
"""