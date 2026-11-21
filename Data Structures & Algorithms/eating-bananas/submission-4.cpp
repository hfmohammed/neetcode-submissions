class Solution {
public:
    int calculate_hours(vector<int>& piles, int limit) {
        if (!limit) return 0;

        cout << limit << endl;
        int total_hours = 0;
        for (int pile : piles) {
            if (pile <= limit) {
                total_hours += 1;
            } else {
                if (limit) total_hours += ((pile + limit - 1) / limit);
            }
        }
        return total_hours;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int max_pile = 0, mid = 0, total_hours = 0;
        for (int pile : piles) max_pile = std::max(max_pile, pile);
        // cout << max_pile << endl;

        int res = -1, left = 1, right = max_pile;
        int count = 0;
        while (left <= right) {
            mid = left + (right - left) / 2;
            // cout << left << " " << mid << " " << right << endl;

            total_hours = calculate_hours(piles, mid);
            cout << "Total_hours: " << total_hours << endl;

            if (left == right) {
                if (total_hours > h) return mid + 1;
                else return mid;
            };

            if (total_hours <= h) {
                right = mid - 1;
                res = mid;
            } else if (total_hours > h) {
                left = mid + 1;
                res = mid;
            }

            mid = left + (right - left) / 2;
            cout << left << " " << mid << " " << right << endl;
            // if (count++ == 100) return 0;

        }
        // binary search from 0 to max_sum and loop over the array to calculate the hours
        return mid;
    }
};
