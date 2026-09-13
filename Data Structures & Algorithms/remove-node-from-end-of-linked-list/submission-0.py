# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)  # initialize dummy node, value is 0 (doesnt matter), and points to head of the actual list
        left = dummy # start left pointer at dummy
        right = head # start right pointer at head

        # while the given int n is greater than 0
        while n > 0:
            right = right.next # we increment the right pointer by one
            n -= 1 # decrement n by 1


        # while right is not null
        while right:
            left = left.next # we increment the left pointer by one
            right = right.next # and continue to increment the right pointer

        left.next = left.next.next # after the loop exits that means the left pointer is at the node before the target node we want to delete
        return dummy.next # so we change that nodes pointer to the one after the target node, effectively deleting the target node


            