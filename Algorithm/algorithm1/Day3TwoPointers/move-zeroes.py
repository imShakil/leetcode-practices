class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i, node in enumerate(nums):
            if node != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
