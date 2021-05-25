class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list=[]
        for i in range(len(nums)):
            for j in range(1+i,len(nums)):
                res=nums[i]+nums[j]
                if res ==target:
                    list=[i,j]
                    return list
