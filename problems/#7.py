class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            list_num=[]
            result=0
            while x>0 :
                list_num.append(x%10)
                x=int(x/10)
            for i in range(len(list_num)):
                result=result+list_num[i]*10**(len(list_num)-i-1)
        if x<0:
            x=abs(x)
            list_num=[]
            result=0
            while x>0 :
                list_num.append(x%10)
                x=int(x/10)
            for i in range(len(list_num)):
                result=result+list_num[i]*10**(len(list_num)-i-1)
            result=result*(-1)
        max=2**31-1
        min=-2**31
        if result in range(min,max):
            return result
        else:
            return 0
