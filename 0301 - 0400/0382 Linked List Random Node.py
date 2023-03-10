class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.values = []

        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.values)
