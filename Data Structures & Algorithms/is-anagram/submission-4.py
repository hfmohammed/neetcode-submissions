class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        for i in s:
            sCount[i] = sCount.get(i, 0) + 1
        
        tCount = {}
        for i in t:
            tCount[i] = tCount.get(i, 0) + 1
        
        return sCount == tCount