# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def insertNext(self,val):
        if self.next==None:
            self.next=ListNode(val)
        else:
            self.next.insertNext(val)
class Solution:
    def __init__(self):
        self.result=ListNode()
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        while (not(self.isNull(l1) and self.isNull(l2))):

            if self.isNull(l1) and not self.isNull(l2):
                self.result.insertNext(l2.val)
                l2=l2.next
            elif not self.isNull(l1) and self.isNull(l2):
                self.result.insertNext(l1.val)
                l1=l1.next
            else:
                if l1.val < l2.val:
                    self.result.insertNext(l1.val)
                    l1=l1.next
                else:
                    self.result.insertNext(l2.val)
                    l2=l2.next

        return self.result.next

    def isNull(self,linkedlist):
        if linkedlist==None :
            return True
        else:
            return False
