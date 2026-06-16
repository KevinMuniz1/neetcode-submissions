class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        sublist = []

        def backtrack(i):

            if i >= len(nums):
                res.append(sublist.copy())
                return
            
            sublist.append(nums[i])
            backtrack(i + 1)


            sublist.pop()
            backtrack(i +1)
        
        backtrack(0)
        return res


            
            




       
                


        