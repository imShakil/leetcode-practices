class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res = []
        while i <= j:
            x, y = nums[i] * nums[i], nums[j] * nums[j]
            if x > y:
                res.append(x)
                i += 1
            else:
                res.append(y)
                j -= 1
        return res[::-1]
