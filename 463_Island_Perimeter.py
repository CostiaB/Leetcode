"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0
represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
 One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
 Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            perimeter = dfs(i, j + 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i - 1, j)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

test0 = {
    'input': {'grid': [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    },
    'output': 16
}

test1 = {
    'input': {'grid': [[1]]
    },
    'output': 4
}
test2 = {
    'input': {'grid': [[1, 0]]
    },
    'output': 4
}

tests = [test0, test1, test2]

for test in tests:
    print(Solution().islandPerimeter(**test['input']) == test['output'])

"""
Runtime 445ms Beats 36.84% of users with Python3
Memory 23.89MB Beats 11.82% of users with Python3
"""