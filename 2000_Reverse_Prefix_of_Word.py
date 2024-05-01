"""
2000. Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the
index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at
    3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:
    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        idx = word.find(ch)
        if idx == -1: return word
        s = list(word[:idx + 1])
        e = list(word[idx + 1:])
        s.reverse()
        return "".join(s + e)

test0 = {
    'input': {'word': "abcdefd",
              'ch': "d"

    },
    'output': "dcbaefd"
}
test1 = {
    'input': {'word': "xyxzxe",
              'ch': "z"

    },
    'output': "zxyxxe"
}
test2 = {
    'input': {'word': "abcd",
              'ch': "z"

    },
    'output': "abcd"
}


tests = [test0, test1, test2]

for test in tests:
    print(Solution().reversePrefix(**test['input']) == test['output'])

"""
Runtime 34ms Beats 63.06% of users with Python3
Memory 16.64MB Beats 9.30% of users with Python3
"""