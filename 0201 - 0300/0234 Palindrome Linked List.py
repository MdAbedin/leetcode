class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return (nums := [node.val for node in takewhile(lambda x: x,accumulate(repeat(head),lambda x,_: x.next))]) == nums[::-1]
