# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def print_list(node):
    if node is None:
        print("NULL")
    else:
        print(node.val, end="->")
        print_list(node.next)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        carry = False
        temp = ListNode(0)
        temp.next = l1
        while curr1 is not None and curr2 is not None:
            curr1.val += curr2.val
            if carry:
                curr1.val += 1
            carry = curr1.val >= 10
            curr1.val %= 10
            temp = curr1
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1 is None and curr2 is None:
            if carry:
                temp.next = ListNode(0)
        elif curr1 is None:
            temp.next = curr2
        
        print_list(l1)
        while carry:
            temp = temp.next
            temp.val += 1
            carry = temp.val >= 10
            if temp.next is None and carry:
                temp.next = ListNode(0)
            temp.val %= 10
            
        return l1
