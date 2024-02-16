"""
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.



Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^9
    0 <= k <= arr.length

"""
from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)

        res = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res

# testcase 1  arr = [5, 5, 4]  k = 1 ans = 1
ans = Solution().findLeastNumOfUniqueInts([5, 5, 4] , 1)
print(ans)

# testcase 2  arr = [4,3,1,1,3,3,2]  k = 3 ans = 2
ans = Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)
print(ans)

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        freq = Counter(arr)
        freq_list = [0] * (len(arr) + 1) # No of elements with that freq


        for n, f in freq.items():
            freq_list[f] += 1
        res = len(freq)

        for f in range(1, len(freq_list)):
            remove = freq_list[f]
            if k >= f * remove:
                k -= f * remove
                res -= remove
            else:
                 remove = k // f
                 res -= remove
                 break
        return res

# testcase 1  arr = [5, 5, 4]  k = 1 ans = 1
ans = Solution().findLeastNumOfUniqueInts([5, 5, 4] , 1)
print(ans)

# testcase 2  arr = [4,3,1,1,3,3,2]  k = 3 ans = 2
ans = Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)
print(ans)


"""
Runtime 345ms Beats 63.98% of users with Python3
Memory 33.60MB Beats 75.99% of users with Python3
"""

"""
Runtime
317ms Beats 91.68% of users with Python3
Memory 33.24MB Beats 94.54% of users with Python3
"""