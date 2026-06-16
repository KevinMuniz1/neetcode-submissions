class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0

        L = 0
        R = 1
        while R < len(s):
            
            print(ord(s[R]))
            score += abs(ord(s[R]) - ord(s[L]))
            print("curr score", score)
            L += 1
            R += 1

        return score
        