# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2, carry = l1,l2,0        
        p = res = ListNode(0)
        
        while p1 or p2 or carry:
            v1 = v2 = 0
            
            if p1: 
                v1 = p1.val
                p1 = p1.next
            
            if p2:
                v2 = p2.val
                p2 = p2.next

            carry,quo = divmod(v1 + v2 + carry,10)
            
            p.next = ListNode(quo)
            
            p = p.next
            
        
        
        return res.next
            
        