class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1"

        ans = ":;".join(strs)
        print(ans)
        return ans
    
    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []

        ans = s.split(":;")

        print(ans)
        return ans