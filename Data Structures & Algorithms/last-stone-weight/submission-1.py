class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            y = max(stones)
            stones.remove(max(stones))
            x = max(stones)
            stones.remove(max(stones))
            if x == y:
                continue
            elif x < y:
                stones.append(y - x)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

        
        





        