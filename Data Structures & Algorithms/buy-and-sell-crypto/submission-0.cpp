class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0], max_price = prices[0], max_profit = 0;

        for (int i : prices) {
            cout << "min_price: " << min_price << " max_price: " << max_price << " max_profit: " << max_profit << endl; 
            if (i < min_price) {
                max_price = i;
                min_price = i;
            } else {
                max_price = max(i, max_price);
                max_profit = max(max_profit, max_price - min_price);
            }
        }
        
        return max_profit;
    }
};
