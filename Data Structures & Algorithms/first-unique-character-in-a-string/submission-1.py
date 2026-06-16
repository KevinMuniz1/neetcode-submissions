from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:


        seen = defaultdict(int)

        for i in range(len(s)):

            seen[s[i]] += 1
        
        for index, value in enumerate(s):
            if seen[value] == 1:
                return index

        return -1



        