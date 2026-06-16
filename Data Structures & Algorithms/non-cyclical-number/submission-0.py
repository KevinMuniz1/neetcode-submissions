class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        temp = 0

        while n != 1:
            n = str(n)
            for i in range(len(n)):
                temp += int(n[i]) ** 2
            if temp in seen:
                return False
            else:
                seen.add(temp)
                n = temp
                temp = 0
        return True
        