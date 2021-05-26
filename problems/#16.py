class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        diff = 100000
        res = int()

        for i,n in  enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l ,r = i+1 , len(nums) - 1
            while l < r:
                threesum = n + nums[l] + nums[r]
                if threesum < target:
                    if diff > target - threesum:
                        diff = target - threesum
                        res = threesum
                    l += 1
                elif threesum > target:
                    if diff > threesum - target:
                        diff = threesum - target
                        res = threesum
                    r -= 1
                else:
                    return threesum

        return res
