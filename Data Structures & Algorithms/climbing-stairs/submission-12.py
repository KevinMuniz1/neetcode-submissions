class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
    
        def dfs(i):

            if i in cache:
                return cache[i]

            elif i <= 1:
                return 1
            else:
                cache[i] = dfs(i -1) + dfs(i - 2)
                return cache[i]
                
        return dfs(n)



        

        