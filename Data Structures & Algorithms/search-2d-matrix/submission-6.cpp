class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n_rows = matrix.size(), n_cols = matrix[0].size();
        int up = 0, down = n_rows - 1, left = 0, right = n_cols - 1, mid_row = 0, mid_col = 0;

        while (up <= down) {
            mid_row = up + (down - up) / 2;
            cout << "up: " << up << ", mid_row: "  << mid_row << ", down: " << down << endl;
            
            if (matrix[mid_row][0] <= target && target <= matrix[mid_row][n_cols - 1]) {
                while (left <= right) {
                    mid_col = left + (right - left) / 2;
                    cout << "left: " << left << ", mid_col: "  << mid_col << ", right: " << right << ", val: " << matrix[mid_row][mid_col] << endl;

                    if (left == right && matrix[mid_row][mid_col] != target) return 0;

                    if (matrix[mid_row][mid_col] == target)
                        return 1;
                    else if (matrix[mid_row][mid_col] < target)
                        left = mid_col + 1;
                    else if (matrix[mid_row][mid_col] > target)
                        right = mid_col - 1;
                }
                return 0;
            } else if (target < matrix[mid_row][0])
                down = mid_row - 1;
            else if (matrix[mid_row][n_cols - 1] < target)
                up = mid_row + 1;

        }
        return 0;
    }
};
