"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n)

        prev = None
        res = ''
        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt !=0:
                prev = [cnt, char]
        return res


test0 = {
    'input': {'s': "aab",

    },
    'output': "aba"
}
test1 = {
    'input': {'s': "aaab",

    },
    'output': ""
}

tests = [test0, test1]

for test in tests:
    print(Solution().reorganizeString(**test['input']) == test['output'])


"""
Runtime 23ms Beats99.61% of users with Python3
Memory 16.59MB Beats 81.06% of users with Python3
"""