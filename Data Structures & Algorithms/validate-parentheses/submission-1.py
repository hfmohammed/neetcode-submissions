class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        
        for i in s:
            if i in "{[(":
                res.append(i)

            elif i in "}])":
                if len(res) == 0:
                    return False

                if (res[-1] == "{" and i == "}") or (
                    res[-1] == "[" and i == "]") or (
                    res[-1] == "(" and i == ")"):
                    res.pop()
                else:
                    return False

            else:
                raise ValueError("Invalid string char:", i)
        
        if res != []:
            return False

        return True