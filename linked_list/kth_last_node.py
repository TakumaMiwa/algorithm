def kth_last_node(k, head):
    fast = slow = head
    for _ in range(k):
        fast = fast.next
    while fast:
        fast, slow = fast.next, slow.next
    return slow

## test
from listnode import ListNode 
l = [1, 3, 5, 7, 9]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next
print(kth_last_node(3, head).data)