# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        self.node = []
        for l in lists:
            while l :
                self.node.append(l.val)
                l = l.next
        self.head = self.result = ListNode(0)
        for x in sorted(self.node):
            self.result.next = ListNode(x)
            self.result =self.result.next
        return self.head.next
