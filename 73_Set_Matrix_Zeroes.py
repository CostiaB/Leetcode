"""
73. Set Matrix Zeroes
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
 Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_h = set()
        zeroes_v = set()

        for v in range(len(matrix)):
            for h in range(len(matrix[0])):
                if matrix[v][h] == 0:
                    zeroes_h.add(h)
                    zeroes_v.add(v)
        for v in range(len(matrix)):
            for h in range(len(matrix[0])):
                if h in zeroes_h or v in zeroes_v:
                    matrix[v][h] = 0
        return matrix

test0 = {
    'input': {'matrix': [[1,1,1],[1,0,1],[1,1,1]]

    },
    'output': [[1,0,1],[0,0,0],[1,0,1]]
}
test1 = {
    'input': {'matrix': [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    },
    'output': [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
}


tests = [test0, test1]

for test in tests:
    print(Solution().setZeroes(**test['input']) == test['output'])

"""
Runtime 100ms Beats 72.37% of users with Python3
Memory 17.70MB Beats 9.35% of users with Python3
"""