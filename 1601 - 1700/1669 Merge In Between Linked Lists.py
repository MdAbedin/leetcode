class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node_a_prev = list1
        for i in range(a-1): node_a_prev = node_a_prev.next
        
        node_b_next = list1
        for i in range(b+1): node_b_next = node_b_next.next

        list2_tail = list2
        while list2_tail.next: list2_tail = list2_tail.next

        node_a_prev.next = list2
        list2_tail.next = node_b_next

        return list1
