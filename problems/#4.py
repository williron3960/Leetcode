class Solution:
    def __init__(self):
        self.result=list()
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens=len(nums1+nums2)
        while len(nums1)!=0 and len(nums2)!=0:
            if nums1[0]>nums2[0]:
                temp=nums2.pop(0)
            else:
                temp=nums1.pop(0)
            self.result.append(temp)
        if len(nums1)==0:
            self.result=self.result+nums2
        else:
            self.result=self.result+nums1

        if lens%2==1:
            res=self.result[int((lens+1)/2)-1]
        else:
            res=(self.result[int(lens/2)-1]+self.result[int((lens/2)+1)-1])/2
        return res
