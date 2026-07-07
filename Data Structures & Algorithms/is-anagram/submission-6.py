from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sHash = defaultdict(int)

        tHash = defaultdict(int)

        for char in s:
            sHash[char] += 1
        
        for char in t:
            tHash[char] += 1
        
        return tHash == sHash


        