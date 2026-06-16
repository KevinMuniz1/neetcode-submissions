class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = {}
        tDic = {}
        for i in range(len(s)):
            char = s[i]
            if char not in sDic:
                sDic[char] = 1
            else:
                sDic[char] += 1
        for i in range(len(t)):
            char = t[i]
            if char not in tDic:
                tDic[char] = 1
            else:
                tDic[char] += 1
        print(sDic)
        print(tDic)
        return sDic == tDic
                      

        