class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        n = bin(n)

        for i in range(len(n)):
            if n[i] == "1":
                count += 1
        
        return count
        