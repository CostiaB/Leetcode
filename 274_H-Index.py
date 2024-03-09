"""
274. H-Index
Solved
Medium
Topics
Companies
Hint

Given an array of integers citations where citations[i] is the number of citations a researcher received for their
ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such
that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two
with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000
"""

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        max_index = len(citations)
        for s in citations:
            if s < max_index:
                max_index -=1

        return max_index

test0 = {
    'input': {
        'citations': [3, 0, 6, 1, 5]
            },
    'output': 3
}

test1 = {
    'input': {
        'citations': [1, 3, 1]
            },
    'output': 1
}
tests = [test0, test1]

for test in tests:
    print(Solution().hIndex(**test['input']) == test['output'])

"""
Runtime 40ms Beats 64.57% of users with Python3
Memory 16.85MB Beats79.31% of users with Python3
"""