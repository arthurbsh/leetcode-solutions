# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = head
        
        while previousNode != None:
            currentNode = previousNode.next
            
            if currentNode != None and currentNode.val == previousNode.val:
                previousNode.next = currentNode.next
            else:
                previousNode = currentNode
                
        return head