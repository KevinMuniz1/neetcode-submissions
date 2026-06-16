class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binn = bin(n)
        for i in range(2, len(str(binn))):
            if binn[i] == "1":
                count += 1
        return count


