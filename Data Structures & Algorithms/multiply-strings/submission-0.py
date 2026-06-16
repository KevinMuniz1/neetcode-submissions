class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1Int = 0

        num2Int = 0

        for i in range(len(num1)):

            num1Int = num1Int * 10 + int(num1[i])
        
        for i in range(len(num2)):

            num2Int = num2Int * 10 + int(num2[i])
        

        return str(num1Int * num2Int)
        
        

        