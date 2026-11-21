class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> data;
        for (auto& a : s) {
            if (data.find(a) == data.end()) {
                data[a] = 0;
            } data[a]++;
        }

        for (char a : t) {
            if (data.find(a) == data.end()) {
                return false;
            } else {
                data[a]--;
            }
        }

        for (auto& [key, value] : data) {
            cout << key << ":" << value << endl;
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
};
