# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        if length-n==0:
            return head.next
        temp = head
        goal = length-n
        curr=0
        while temp:
            curr+=1
            if curr==goal:
                break
            temp = temp.next
        
        temp.next = temp.next.next if temp.next else None

        return head
