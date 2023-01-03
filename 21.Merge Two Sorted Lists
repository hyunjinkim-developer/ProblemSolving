# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list2 is not None:
            nodeA, nodeB = list1, list2
            list2 = list2.next

            if nodeB.val <= nodeA.val:
                nodeB.next = nodeA
                list1 = nodeB
            else:
                prev = None
                while nodeA is not None and nodeB.val > nodeA.val:
                    prev = nodeA
                    nodeA = nodeA.next
                
                temp = prev.next
                prev.next = nodeB
                nodeB.next = temp

        return list1
