"""
2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.



Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.


"""

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            ans = self.checkIfPaly(w)
            if ans == 1:
                return w
        return ""

    def checkIfPaly(self, word):
        if word[::-1] == word:
            return 1
        else:
            return 0


# test case 1: ["abc","car","ada","racecar","cool"]  ans = "ada"
ans = Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"])
print(ans)
# test case 2: ["notapalindrome", "racecar"]   ans = "racecar"
ans = Solution().firstPalindrome(["notapalindrome", "racecar"])
print(ans)
# test case 3: ["def", "ghi"]  ans=""
ans = Solution().firstPalindrome(["def", "ghi"])
print(ans)