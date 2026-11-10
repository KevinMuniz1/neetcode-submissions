class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = {}
        res = []

        for word in strs:
            tempWord = "".join(sorted(word))
            if tempWord in buckets:
                buckets[tempWord].append(word)
            else:
                buckets[tempWord] = []
                buckets[tempWord].append(word)

        for value in buckets.values():
            res.append(value)
        
        return res
        
        







        