class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        peopleHeights = zip(names,heights)

        peopleHeights = sorted(peopleHeights, key = lambda x: x[1], reverse = True)

        return [name for name,heights in peopleHeights]
        