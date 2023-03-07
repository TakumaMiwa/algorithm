def right_shift(head, k):
    p, length = head.next, 0
    while p:
        length += 1
        p = p.next
    k %= length
    p = head
    for _ in range(k-1):
        p = p.next
    dummy_head = ListNode(0, p.next)
    p.next = None
    p = dummy_head
    while p.next:
        p = p.next
    p.next = head.next
    return dummy_head

## test
from listnode import ListNode 
l = [2, 3, 5, 3, 2]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next

aft_head = right_shift(head, 8).next
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next
