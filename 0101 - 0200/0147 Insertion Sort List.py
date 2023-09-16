class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None,head)
        i = 0

        while True:
            cur = head
            for i2 in range(i): cur = cur.next

            node = cur.next
            if not node: break
            cur.next = cur.next.next

            cur = head
            
            for i2 in range(i):
                if cur.next.val < node.val: cur = cur.next
                else: break

            node.next = cur.next
            cur.next = node

            i += 1

        return head.next
