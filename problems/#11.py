class Solution:
    def __init__(self):
        self.area=0
        self.l=0
    def maxArea(self, height: List[int]) -> int:
        self.r=len(height)-1
        while self.l<self.r:
            self.area=max(self.area,
                          min(height[self.l],height[self.r])*(self.r-self.l))
            if  height[self.l]<height[self.r]:
                self.l+=1
            else:
                self.r-=1
        return self.area
