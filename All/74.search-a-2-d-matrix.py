#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                lo = 0
                hi = len(matrix[i])-1
                
                while lo <= hi:
                    mid = (lo+hi)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
       return False 
# @lc code=end

