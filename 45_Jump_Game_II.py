"""
45. Jump Game II
Solved
Medium
Topics
Companies

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such
that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


"""
class Solution:
    def jump(self, nums: list[int]) -> int:
        # pointers to show current range of indices
        l, r = 0, 0
        ans = 0
        # while r les than last index
        while r < (len(nums) - 1):
            maxJump = 0
            # iteration between l and r
            for i in range(l, r + 1):
                # searching the max jumping distance in current range
                maxJump = max(maxJump, i + nums[i])
            # moving the left pointer to the end of current range
            l = r + 1
            # update the left pointer to maximum jump distance
            r = maxJump
            ans += 1
        return ans

test0 = {
    'input': {
        'nums': [2, 3, 1, 1, 4]
            },
    'output': 2
}

test1 = {
    'input': {
        'nums': [2, 3, 0, 1, 4]
            },
    'output': 2
}

tests = [test0, test1]

for test in tests:
    print( Solution().jump( **test['input'] ) == test['output'])



"""
Runtime 95ms Beats96.26% of users with Python3
Memory 17.58MB Beats79.25% of users with Python3
"""
