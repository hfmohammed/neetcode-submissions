class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = -1

        while begin < len(s) / 2 and (-end - 1) < len(s) / 2:
            print(begin)
            print(end)

            if not s[begin].isalnum():
                begin += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[begin].lower() != s[end].lower():
                print(s[begin].lower())
                print(s[end].lower())

                return False

            begin += 1
            end -= 1
        return True