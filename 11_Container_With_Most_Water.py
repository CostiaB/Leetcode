"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""


class Solution:

    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        amt = 0
        while l < r:
            amt = max(amt, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return amt

test0 = {
    'input': {'height': [1, 8, 6, 2, 5, 4, 8, 3, 7]

    },
    'output': 49
}
test1 = {
    'input': {'height': [1, 1]

    },
    'output': 1
}


tests = [test0, test1]

for test in tests:
    print(Solution().maxArea(**test['input']) == test['output'])

"""
Runtime 524ms Beats 59.65% of users with Python3
Memory 29.48MB Beats 78.26% of users with Python3
"""