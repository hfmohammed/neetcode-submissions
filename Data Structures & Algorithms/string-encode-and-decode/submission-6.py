class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1"

        # for i in range(len(strs)):
        #     strs[i] = str(len(strs[i])) + strs[i]

        ans = ":;".join(strs)
        print(ans)
        return ans
    
    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []

        ans = s.split(":;")
        # for i in range(len(s)):
        #     strs[i] = 
        # if ans[0] == '':
        #     ans = []
        print(ans)
        return ans