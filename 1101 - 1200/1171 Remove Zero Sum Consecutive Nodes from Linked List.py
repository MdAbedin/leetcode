# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        sums = deque([0])
        sum_last_nodes = {0: dummy}
        
        while cur.next:
            next_sum = sums[-1] + cur.next.val
            
            if next_sum in sum_last_nodes:
                while sums[-1] != next_sum:
                    sum_last_nodes.pop(sums.pop())
                sum_last_nodes[next_sum].next = cur.next.next
                cur = sum_last_nodes[next_sum]
            else:
                sums.append(next_sum)
                cur = cur.next
                sum_last_nodes[next_sum] = cur
                
        return dummy.next
