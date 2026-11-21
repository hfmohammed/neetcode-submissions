#include <unordered_map>

class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> _time_map;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        _time_map[key].push_back({ timestamp, value });
    }
    
    string get(string key, int timestamp) {
        size_t m_size = _time_map[key].size();
        string res = "";
        if (m_size == 0) {
            return res;
        }

        int left = 0, right = m_size - 1, mid = 1;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (_time_map[key][mid].first <= timestamp) {
                res = _time_map[key][mid].second;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return res;
    }
};