def remove_dup(head):
    key = p = head.next
    while key:
        while p and key.data == p.data:
            p = p.next
        key.next = p
        key = p
    return head

## test
from listnode import ListNode 
l = [1, 1, 1, 3, 3,  7, 9]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next

aft_head = remove_dup(head)
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next