class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNums = sorted(nums)
        numDict = {}
        kElements = []
        for i in range(len(sortedNums)):
            if sortedNums[i] not in numDict:
                numDict[sortedNums[i]] = 1
            else:
                numDict[sortedNums[i]] += 1
        sortedDict = dict(sorted(numDict.items(), key=lambda item: item[1]))
        for i in range(k):
            key, value = sortedDict.popitem()
            kElements.append(key)
        return kElements
        



                