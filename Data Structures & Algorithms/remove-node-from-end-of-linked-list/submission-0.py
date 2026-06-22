# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count+=1
            cur = cur.next
        need = count-n

        if need ==0:
            return head.next
        
        current = head
        for _ in range (need-1):
            if current is None or current.next is None:
                return head
            current=current.next
        if current.next:
            current.next = current.next.next
        return head