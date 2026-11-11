class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = "".join(s.split()).lower()

        l = 0
        r = (len(newS) - 1 )

        while l < r:
            if not newS[l].isalnum():
                l += 1
                continue
            elif not newS[r].isalnum():
                r -= 1
                continue
            elif newS[l] !=  newS[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
            





        