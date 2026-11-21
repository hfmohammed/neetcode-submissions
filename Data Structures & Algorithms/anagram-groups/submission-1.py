class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        read = set()

        for idx, s in enumerate(strs):
            if idx not in read:
                temp = []
                sortedS = "".join(sorted(s))
                temp.append(s)
                read.add(idx)
                for j in range(idx + 1, len(strs)):
                    if "".join(sorted(strs[j])) == sortedS and j not in read:
                        temp.append(strs[j])
                        read.add(j)

                output.append(temp)

        
        return output