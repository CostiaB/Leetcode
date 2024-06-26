"""
2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid.
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
  maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Example 1:
Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

Example 2:
Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

Constraints:

    n == grid.length == grid[i].length
    3 <= n <= 100
    1 <= grid[i][j] <= 100
"""


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid) - 2

        maxLocal = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        maxLocal[i][j] = max(
                            maxLocal[i][j],
                            grid[r][c]
                        )

        return maxLocal

test0 = {
    'input': {'grid': [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]


    },
    'output': [[9,9],[8,6]]
}
test1 = {
    'input': {'grid': [[1,1,1,1,1], [1,1,1,1,1], [1,1,2,1,1], [1,1,1,1,1], [1,1,1,1,1]]

    },
    'output': [[2,2,2], [2,2,2], [2,2,2]]
}


tests = [test0, test1]

for test in tests:
    print(Solution().largestLocal(**test['input']) == test['output'])


"""
Runtime 155ms Beats 12.77% of users with Python3
Memory 17.08MB Beats 70.30% of users with Python3
"""