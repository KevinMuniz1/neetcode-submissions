class Solution:
    def isPalindrome(self, x: int) -> bool:

        stringX = str(x)

        L = 0 

        R = len(stringX) - 1

        while L < R:
            if stringX[L] != stringX[R]:
                return False
            else:
                L += 1
                R -= 1
        
        return True
        