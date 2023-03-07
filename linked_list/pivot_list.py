def pivot_list(head, k):
    pivot = head
    for _ in range(k): pivot = pivot.next

    pre, mid, post = ListNode(), ListNode(), ListNode()
    dummy_head_pre, dummy_head_mid, dummy_head_post= pre, mid, post
    p = head.next
    while p:
        if p.data < pivot.data:
            pre.next = p
            pre = pre.next
        elif p.data == pivot.data:
            mid.next = p
            mid = mid.next
        else:
            post.next = p
            post = post.next
        p = p.next
    post.next = None
    pre.next = dummy_head_mid.next
    mid.next = dummy_head_post.next
    return dummy_head_pre



## test
from listnode import ListNode 
l = [6, 5, 4, 3, 2, 1, 3]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next

aft_head = pivot_list(head, 4).next
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next