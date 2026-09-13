# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
            dummy = node = ListNode()  # create one node but two refrences to that node

            while list1 and list2: # while both list have nodes in them
                if list1.val < list2.val:  # depending on the smaller initial node, that will become the head of the new merged list
                    node.next = list1  # the next node is whatever is the initial node in list1
                    list1 = list1.next # then you iterate the first node in list1 to the second node in that list
            
                else:
                    node.next = list2
                    list2 = list2.next

                node = node.next  # iterate the node in the merged list to the next one

            node.next = list1 or list2   # this accounts for if one list ends before the other, you appened the rest of the ongoing list into the merged list

            return dummy.next   # return the next node after the dummy node, the dummy node being the head of the merged list



        


        