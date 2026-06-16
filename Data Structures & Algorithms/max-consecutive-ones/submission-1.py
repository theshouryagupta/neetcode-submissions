class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current > result:
                    result = current
            else:
                current = 0
        return result