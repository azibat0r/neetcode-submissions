class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l2 = 0
                r2 = len(matrix[mid]) - 1
                while l2 <= r2:
                    d = (l2 + r2) // 2
                    if matrix[mid][d] == target:
                        return True
                    elif matrix[mid][d] > target:
                        r2 = d - 1
                    else:
                        l2 = d + 1
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False