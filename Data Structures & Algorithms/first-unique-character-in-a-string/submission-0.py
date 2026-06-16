from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] += 1
        
        for i in range(len(s)):

            char = s[i]

            if count[char] == 1:
                return i
        
        return -1

        