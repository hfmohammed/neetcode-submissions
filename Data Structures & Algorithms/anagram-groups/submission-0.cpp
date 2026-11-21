class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map< map<char, int>, vector<string> > data;
        map<char, int> m;

        for (string s : strs) {
            m.clear();
            for (char c : s) {
                if (m.find(c) == m.end()) {
                    m[c] = 0;
                } m[c]++;
            }
            if (data.find(m) == data.end()) {
                data[m] = vector<string>{};
            } data[m].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& [key, value] : data) {
            ans.push_back(value);
        }

        return ans;
    }
};
