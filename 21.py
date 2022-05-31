# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.list1 = None
        self.list2 = None
       
    
    def useFirst(self):
        return self.list1.val <= self.list2.val
            
        
    def addFromFirst(self):
        if (self.head == None):
            self.head = self.list1
            self.tail = self.head
            
        else:
            self.tail.next = self.list1 #connect tail
            self.tail = self.tail.next #move tail
        
        self.list1 = self.list1.next #move list
        self.tail.next = None #cut list
    
    def addFromSecond(self):
        if (self.head == None):
            self.head = self.list2
            self.tail = self.head
        else:
        
            self.tail.next = self.list2 #connect tail
            self.tail = self.tail.next #move tail
        self.list2 = self.list2.next #move list
        self.tail.next = None #cut list
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        self.list1 = list1
        self.list2 = list2
        
        while(self.list1 and self.list2):
            if self.useFirst():
                self.addFromFirst()
            else:
                self.addFromSecond()
                
        if self.list1 or self.list2:
            self.tail.next = self.list1 if self.list1 else self.list2
        
        return self.head.next