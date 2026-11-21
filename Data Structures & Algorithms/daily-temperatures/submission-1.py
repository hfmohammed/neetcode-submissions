class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        noneItems = set()
        out = []
        for i in range(len(temperatures)):
            out.append(0)
            noneItems.add(i)
            print(i)

            copyNoneItems = noneItems.copy()
            for j in copyNoneItems:
                print(j)

                if len(noneItems) == 0:
                    break
                
                if out[j] == 0 and temperatures[j] < temperatures[i]:
                    out[j] = i - j
                    noneItems.remove(j)
        
        return out