# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head 
        prev = ListNode() 
        while curr != None: 
            if curr.val == val:
                if head == curr: 
                    head = curr.next
                # remove the node 
                prev.next = curr.next
            else: 
                prev = curr
            curr = curr.next 
        return head
