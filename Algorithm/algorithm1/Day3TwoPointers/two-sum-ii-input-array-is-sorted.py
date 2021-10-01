class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lo = 0
        hi = len(numbers) - 1

        while lo < hi:
            x = numbers[lo] + numbers[hi]
            if x == target:
                return [lo + 1, hi + 1]
            elif x > target:
                hi -= 1
            else:
                lo += 1
