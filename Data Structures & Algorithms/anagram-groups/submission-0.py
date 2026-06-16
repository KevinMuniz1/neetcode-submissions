from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordMap = defaultdict(list)

        for w in strs:
            sortedWord = "".join(sorted(w)) 
            wordMap[sortedWord].append(w)
        
        return list(wordMap.values())
        
            


        
            



        

            
        

        

        
        
            

        
