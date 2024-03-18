"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        ans = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]

        return ans

test0 = {
    'input': {'height': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    },
    'output': 6
}
test1 = {
    'input': {'height': [4, 2, 0, 3, 2, 5],

    },
    'output': 9
}

tests = [test0, test1]

for test in tests:
    print(Solution().trap(**test['input']) == test['output'])

"""
Runtime 103ms Beats55.13% of users with Python3
Memory 18.52MB Beats40.20% of users with Python3
"""