# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        fast = slow = first = head
        
        i = 1
        while i < k:
            fast = fast.next
            first =first.next
            
            i +=1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        first.val, slow.val = slow.val, first.val
        
        return head
            
            
        