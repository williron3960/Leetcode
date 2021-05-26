class Solution:
    def fourSum(self, nums, target: int) :
        if not nums:
            return list()

        res = list()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target_diff = target - nums[i]
            for j in range(i+1 ,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l , k = j+1 , len(nums) - 1
                while l < k:
                    foursum = nums[i] + nums[j] + nums[l] + nums[k]
                    if foursum < target:
                        l += 1
                    elif foursum > target:
                        k -= 1
                    else:
                        res.append([nums[i] , nums[j] , nums[l] , nums[k]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < k:
                            l += 1

        return res
