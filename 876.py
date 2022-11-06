# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        while head:
            ls.append(head)
            head=head.next
        idx=len(ls)//2
        
        if idx>0:
            return ls[idx-1].next
        else:
            return ls[0]
        
