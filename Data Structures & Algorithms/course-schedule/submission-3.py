class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preCrs = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preCrs[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            nonlocal visiting

            if crs in visiting:
                return False
            
            if preCrs[crs] == []:
                return True
            
            visiting.add(crs)
            
            for pre in preCrs[crs]:

                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            
            preCrs[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        




        