# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if (head==None):
            return None
        if (left==right):
            return head
        
        t=head
        before=None
        pos=1

        while(pos<left):
            before=t
            t=t.next
            pos+=1

        curr=t
        prev=None
        times=right-left+1
        while(times):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            times-=1
        
        t.next=curr
        if(before):
            before.next=prev
            return head
        else:
            return prev
