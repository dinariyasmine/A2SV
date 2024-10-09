# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head 
        def Mil(head): 
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = Mil(head)
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)



        def merge(left, right):
            x = ListNode(0)
            inter = x
            while left and right:
                if left.val < right.val:
                    inter.next = left
                    left = left.next
                else:
                    inter.next = right
                    right = right.next
                inter = inter.next

            if left:
                inter.next = left
            if right:
                inter.next = right
            return x.next
        return merge(left, right)