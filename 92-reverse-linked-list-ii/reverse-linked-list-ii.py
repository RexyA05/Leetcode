# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0,head)
        leftPrev,curr=dummy,head
        #Reach node at position "left"
        for i in range(left-1):
            leftPrev=curr
            curr=curr.next
        #Now curr="left" and leftPrev="Node before left"
        #Reverse from left to right
        prev=None
        for i in range(right-left+1):
            tmpNxt=curr.next
            curr.next=prev
            prev,curr=curr,tmpNxt
        #update pointers
        leftPrev.next.next=curr
        leftPrev.next=prev
        return dummy.next