#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        tot = 0
        for row in grid:
            lo = 0
            hi = len(row) - 1
            while lo <= hi:
                mid = (lo+hi)//2
                if row[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
            print(lo, hi)
            tot += (len(row) - lo)
        return tot
        
# @lc code=end

