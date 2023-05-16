# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Запускаю два поинтера, один - с начала, другой - с середины.


head = [1,2,2,1]


def isPalindrome(head):
    if not head or len(head) == 1:
        return True
   
    left = 0
    right = len(head) - 1
 
    while left < right:
        if head[left] != head[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(isPalindrome(head))