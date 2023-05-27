# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        ptr = head
        s = ''
        while ptr:
            print(ptr.val)
            s += str(ptr.val)
            ptr = ptr.next
        return int(s,2)

head5 = ListNode(1)
head4 = ListNode(0, head5)
head3 = ListNode(1, head4)
head2 = ListNode(0, head3)
head1 = ListNode(1, head2)

ans = Solution()
print(ans.getDecimalValue(head1))