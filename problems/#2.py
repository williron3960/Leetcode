# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def insertNext(self,val=0):
        if self.next==None:
            self.next=ListNode(val)
        else:
            self.next.insertNext(val)
class Solution:
    def __init__(self):
        self.result=ListNode()
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str_l1=self.string_l(l1)
        str_l2=self.string_l(l2)
        res=str(int(str_l1)+int(str_l2))
        self.result.val=int(res[-1])
        for i in range(len(res)-2,-1,-1) :
            self.result.insertNext(int(res[i]))
        return self.result
    def string_l(self,l1,str_l=str()):
        if l1 != None:
            str_l=str(l1.val)+str_l
            return self.string_l(l1.next,str_l)
        else:
            return str_l
