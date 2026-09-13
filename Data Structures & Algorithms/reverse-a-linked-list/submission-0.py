# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

       
        curr =  head  # the current pointer is the head of the linked list
        prev = None   # the previous pointer starts at null, which is right before the head


        # continue the loop while current is not null
        while curr:
            
            
            nxt = curr.next # temp variable for next, which stores what the original next node is
            curr.next = prev # reverse current nodes pointer to the previous node
            prev = curr # update previous pointer to be the current node
            curr = nxt # update current pointer to the next node
        return prev
            