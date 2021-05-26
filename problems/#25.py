class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        test_head = head
        for i in range(k):
            if not test_head:
                return head
            test_head = test_head.next
        i = int()
        new_head = self.reverseKGroup(test_head,k)
        while i<k :
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            i += 1
        return new_head
