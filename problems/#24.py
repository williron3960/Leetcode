class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # one and two node
        if not (head and head.next):
            return head
        res = head.next
        temp = head.next.next
        head.next.next = head
        head.next = self.swapPairs(temp)
        return res
