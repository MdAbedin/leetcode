# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution:

    def pairSum(self, head):

        slow = head

        fast = head

        maxVal = 0

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        nextNode, prev = None, None

        while slow:

            nextNode = slow.next

            slow.next = prev

            prev = slow

            slow = nextNode

        while prev:

            maxVal = max(maxVal, head.val + prev.val)

            prev = prev.next

            head = head.next

        return maxVal
