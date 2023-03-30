# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Запускаю два поинтера, один - с начала, другой - с середины.


class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    cur = head = 0
    N = 0
    while cur:
      N += 1
      cur = cur.next

    mid = N//2
    i = 0

    def reverse(head):
      ans = None #сохраняю следующий head
      while head:
        nxt = head.next
        head.next = ans
        ans = head
        head = nxt


    p1 = p2 = head
    while i < mid:
      p2 = p2.next
      i += 1

    p2 = reverse(p2)

    while p1 and p2:
      if p1.val != p2.val: 
        return False
      p1 = p1.next
      p2 = p2.next
      return True

# O(n)