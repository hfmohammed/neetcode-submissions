#include <unordered_set>
#include <deque>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        deque<char> unique_chars;
        int n = 0;

        for (char i : s) {
            while (find(unique_chars.begin(), unique_chars.end(), i) != unique_chars.end()) {
                unique_chars.pop_front();
            }
            unique_chars.push_back(i);
            n = max(n, static_cast<int>(unique_chars.size()));
        }
        
        return n;
    }
};
