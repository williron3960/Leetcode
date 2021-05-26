class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        num_list=[]
        index_list=[]
        for i in range(len(nums)):
            if nums[i]!=nums[i-1]:
                num_list.append(nums[i])
                index_list.append(i)
        index_list.append(len(nums))

        for i in range(len(num_list)):
            for j in range(len(num_list)):
                res=num_list[i]+num_list[j]
                if res==target:
                    if (i!=j) :
                        answer=[min(index_list[i]+1,index_list[j]+1),max(index_list[i]+1,index_list[j]+1)]
                    elif  (i==j and index_list[i+1]-index_list[i]>1):
                        answer=[min(index_list[i]+1,index_list[j]+2),max(index_list[i]+1,index_list[j]+2)]

        return(answer)
