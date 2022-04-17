# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = []
        p = res = ListNode(0)
        
        while head:
            node.append(head.val)
            head = head.next
            
        for val in sorted(node):
            p.next = ListNode(val)
            p = p.next
            
        return res.next
            
        
        
        