class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0

        seen = set()

        L = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[L])
                L += 1
            if s[r] not in seen:
                seen.add(s[r])
                maxLength = max((r - L) + 1, maxLength)
        
        return maxLength

            

            


            

            

        