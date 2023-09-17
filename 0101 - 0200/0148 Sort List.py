class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        ans = ListNode(None,head)
        ans_tail = ans
        size = 2

        while True:
            while ans_tail.next:
                l1 = ans_tail.next
                l1_tail = l1

                for i in range(size//2-1):
                    if not l1_tail.next:
                        if ans_tail == ans: return ans.next
                        break
                    l1_tail = l1_tail.next

                l2 = l1_tail.next
                l1_tail.next = None
                l2_tail = l2

                for i in range(size//2-1):
                    if not l2_tail or not l2_tail.next: break
                    l2_tail = l2_tail.next

                if l2_tail:
                    after = l2_tail.next
                    l2_tail.next = None
                else:
                    after = None

                while l1 and l2:
                    if l1.val < l2.val:
                        ans_tail.next = l1
                        l1 = l1.next
                    else:
                        ans_tail.next = l2
                        l2 = l2.next
                    ans_tail = ans_tail.next

                if l1:
                    ans_tail.next = l1
                    ans_tail = l1_tail
                else:
                    ans_tail.next = l2
                    ans_tail = l2_tail

                ans_tail.next = after

            ans_tail = ans
            size *= 2
