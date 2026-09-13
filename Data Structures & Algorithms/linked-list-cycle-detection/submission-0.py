# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # set both pointers at the start
        fast = head
        slow = head


        # while the fast node exists and the next node to it exists, we loop
        while fast and fast.next:

            
            fast = fast.next.next   # step size 2
            slow = slow.next        # step size 1


            # if at any point as we loop that the two pointers 
            # point to the same node, return true
            if fast == slow:
                return True

        # if the loop exit condition is met (in this case either fast or fast.next is null) 
        # and both pointers did not equal eachother at any point, return false
        return False

        
     