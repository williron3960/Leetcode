class Solution:
    def __init__(self):
        self.now_index = int()
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            if nums[i] >= target :
                return i
        return len(nums)
