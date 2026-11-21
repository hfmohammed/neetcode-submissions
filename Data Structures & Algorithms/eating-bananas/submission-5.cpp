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
                total_hours += ((pile + limit - 1) / limit);
            }
        }
        return total_hours;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        // binary search from 1 to max_sum and loop over the array to calculate the hours for each number

        int max_pile = 0, mid = 0, total_hours = 0;
        for (int pile : piles) max_pile = std::max(max_pile, pile);
        cout << max_pile << endl;

        int left = 1, right = max_pile;
        while (left <= right) {
            mid = left + (right - left) / 2;
            cout << left << " " << mid << " " << right << endl;

            total_hours = calculate_hours(piles, mid);
            cout << "Total_hours: " << total_hours << endl;

            if (left == right) {
                if (total_hours > h) return mid + 1;
                else return mid;
            }

            if (total_hours <= h) {
                right = mid - 1;
            } else if (total_hours > h) {
                left = mid + 1;
            }
        }
        return mid;
    }
};
