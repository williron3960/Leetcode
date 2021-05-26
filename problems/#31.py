class Solution(object):
    def nextPermutation(self, nums):
        pivotFirst=-1
        i=len(nums)-1
        tmp=nums[-1]
        while i>=0:
            if nums[i]>=tmp:
                tmp=nums[i]
                i-=1
            else:
                pivotFirst=i
                break
        if pivotFirst==-1:
            nums.reverse()
            return
        pivotFirst=i
        pivotSecond=-1
        j=len(nums)-1
        while(j>pivotFirst):
            if nums[j]>nums[pivotFirst]:
                pivotSecond=j
                break
            j-=1

        nums[pivotSecond],nums[pivotFirst]=nums[pivotFirst],nums[pivotSecond]
        l,r = pivotFirst+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
