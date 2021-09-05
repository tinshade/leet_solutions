# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Recursive Approach
        '''
        if head == None or head.next == None:
          return head
        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curr 


    def reverseListTwo(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Standard Approach
        '''
        if head == None or head.next == None:
            return head
        prev, curr = None, head
        while curr:
            next_node = curr.next
            print(prev.val, curr.val, next_node.val) #Debugging
            curr.next = prev
            prev = curr
            curr = next_node
            print(prev.val, curr.val) #Debugging

        return prev

