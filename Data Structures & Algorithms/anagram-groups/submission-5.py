class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort in group:
                group[sort].append(word)
            else:
                group[sort] = []
                group[sort].append(word)
        
        return list(group.values())





        