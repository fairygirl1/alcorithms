# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# Запускаю два поитера, один делает два шага, другой - один.
# Если в списке есть цикл, рано или поздно поинтеры сойдутся на одной ноде.

head = [3,2,0,-4]

def hasCycle(head):
  if not head or not head.next:
    return False
  p1 = p2 = head
  while p2 and p2.next:
    p1 = p1.next
    p2 = p2.next.next

    if p1 == p2:
      return True
    
  return False

print(hasCycle(head))

# O(n)