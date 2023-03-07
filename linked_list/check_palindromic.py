def check_palindromic(head):
    p, length = head.next, 0
    while p:
        length += 1
        p = p.next
    stack = []
    p = head.next
    for _ in range(length//2):
        stack.append(p.data)
        p = p.next
    if length%2: p = p.next
    while p:
        node = stack.pop()
        if node != p.data: return False
        p = p.next
    return True

## test
from listnode import ListNode 
l = [2, 3, 5, 3, 2]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next

print(check_palindromic(head))