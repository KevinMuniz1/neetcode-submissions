class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        ## compute prefix
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        
        ## compute postfix to complete answer

        postfix = 1
        for i in range(n)[::-1]:
            res[i] = postfix * res[i]
            postfix *= nums[i]
        
        return res



        

