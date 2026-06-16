
## given an array of strings group all anagrams together in sublist

## we can make a key the sorted version of a word and then have a list be the value

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordHash = {}

        res = []

        for word in strs:

            if "".join(sorted(word)) not in wordHash:
                wordHash["".join(sorted(word))] = [word]
            else:
                wordHash["".join(sorted(word))].append(word)
        
        for key, bucket in wordHash.items():
            res.append(bucket)
        
        return res
        
        
            

        