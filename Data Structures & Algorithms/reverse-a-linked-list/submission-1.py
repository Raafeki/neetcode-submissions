# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        curr = head
        prev = None

        while curr:  #continue loop while curr is not null (while curr exists)
            next_ = curr.next  # here we temporarily store whatever the next node is
            curr.next = prev   # we then  reverse the current node to point at the prev node
            prev = curr        # update the previous node to now be the current node
            curr = next_       # shift the current node to the next node in the list

        return prev
        