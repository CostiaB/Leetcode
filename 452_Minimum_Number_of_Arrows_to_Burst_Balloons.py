"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
 denotes a balloon whose horizontal diameter stretches between xstart and xend.
 You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different
 points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x
  if xstart <= x <= xend. There is no limit to the number of arrows that can be shot.
  A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to
 burst all balloons.



Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
    1 <= points.length <= 105
    points[i].length == 2
    -231 <= xstart < xend <= 231 - 1
"""

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        cnt = len(points)
        points.sort()
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                cnt -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr

        return cnt

test0 = {
    'input': {'points': [[1, 2], [3, 4], [5, 6], [7, 8]]

    },
    'output': 4
}
test1 = {
    'input': {'points': [[1, 2], [2, 3], [3, 4], [4, 5]],

    },
    'output': 2
}
test2 = {
    'input': {'points': [[10, 16], [2, 8], [1, 6], [7, 12]],

    },
    'output': 2
}


tests = [test0, test1, test2]

for test in tests:
    print(Solution().findMinArrowShots(**test['input']) == test['output'])

"""
Runtime 1103ms Beats 34.21% of users with Python3
Memory 62.15MB Beats 91.41% of users with Python3
"""