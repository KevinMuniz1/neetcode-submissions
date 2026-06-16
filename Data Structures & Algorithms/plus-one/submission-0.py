class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = 0

        result = []

        for item in digits:

            res = res * 10 + int(item)
        
        res += 1

        print(res)

        res = str(res)

        for i in range(len(str(res))):
            result.append(int(res[i]))
        
        return result
            



            
        