class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordResult = {}

        res = []

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in wordResult:
                wordResult[sortedWord].append(word)
            else:
                wordResult[sortedWord] = []
                wordResult[sortedWord].append(word)
        
        for sortedWord, wordList in wordResult.items():

            res.append(wordList)
        
        return res
            


        