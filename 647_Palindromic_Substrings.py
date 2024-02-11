"""
647. Palindromic Substrings
Solved
Medium
Topics
Companies
Hint

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.


"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0
        self.L = len(s)

        for i in range(self.L):
            # count odd elements palindromes
            ans += self.countPalindr(s, i, i)
            # count even elements palindromes
            ans += self.countPalindr(s, i, i + 1)
        return ans

    def countPalindr(self, s, l, r):
        res = 0
        while (l >= 0) and (r < self.L) and (s[l] == s[r]):
            res += 1
            l -= 1
            r += 1

        return res


#test case 1 s = 'abc' ans=3
ans = Solution().countSubstrings('abc')
print(ans)

#test case 2 s = 'aaa' ans=6

ans = Solution().countSubstrings('aaa')
print(ans)

"""
Runtime 65ms Beats 97.28% of users with Python3
Memory 16.34MB Beats 94.09% of users with Python3
"""