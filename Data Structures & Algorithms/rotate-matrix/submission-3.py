class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1
        while start < end:
            marker_start = start
            marker_end = end
            while marker_start < end:
                print(start, end, marker_start, marker_end)
                temp = matrix[start][marker_start]
                print("temp:", temp)
                
                print(matrix[start][marker_start], "<-", matrix[marker_end][start])
                matrix[start][marker_start] = matrix[marker_end][start]

                print(matrix[marker_end][start], "<-", matrix[end][marker_end])
                matrix[marker_end][start] = matrix[end][marker_end]

                print(matrix[end][marker_end], "<-", matrix[marker_start][end])
                matrix[end][marker_end] = matrix[marker_start][end]

                print(matrix[marker_start][end], "<-", temp)
                matrix[marker_start][end] = temp

                marker_start += 1
                marker_end -= 1
                print(matrix)
                
            start += 1
            end -= 1
