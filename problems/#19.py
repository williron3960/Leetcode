class Solution:
    def __init__(self):
        self.len=int()
        self.now=int()
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.track(head)     #新增self.len
        if (self.len)>1:
            result= self.remove(head,self.len-n)
            return result
        else:
            return None

    def remove(self,head,n):
        self.now+=1
        if self.now ==n:
            head.next= head.next.next
            return head
        elif self.now ==n+1:
            return head.next
        else:
            head.next=self.remove(head.next,n)
            return head

    def track(self,head):
        if head!=None:
            self.len+=1
            self.track(head.next)
        else:
            return
