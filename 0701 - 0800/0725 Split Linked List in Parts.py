class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        part_length,bigger_parts = divmod(length,k)
        node = head
        ans = []

        for i in range(k):
            if not node:
                ans.append(None)
                continue
                
            head = node
            
            for i2 in range(part_length + (len(ans) < bigger_parts) - 1): node = node.next
            
            nxt = node.next
            node.next = None
            ans.append(head)
            node = nxt

        return ans
