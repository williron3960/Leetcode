class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp

        return new_head
