"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if l not in magazine:
                return False
            magazine = magazine.replace(l, "", 1)
        return True


test0 = {
    'input': {'ransomNote': "a",
              'magazine': "b"
    },
    'output': False
}

test1 = {
    'input': {'ransomNote': "aa",
              'magazine': "ab"
    },
    'output': False
}
test2 = {
    'input': {'ransomNote': "aa",
              'magazine': "aab"
    },
    'output': True
}

tests = [test0, test1, test2]

for test in tests:
    print(Solution().canConstruct(**test['input']) == test['output'])


"""
Runtime 38ms Beats 96.24%of users with Python3
Memory 16.66MB Beats 84.09% of users with Python3
"""