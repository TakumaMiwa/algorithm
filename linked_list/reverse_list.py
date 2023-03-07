from listnode import ListNode

def reverse_list(head):
    pre, mid, post = head.next, head.next.next, head.next.next.next
    pre.next = None
    while post:
        mid.next = pre
        pre, mid, post = mid, post, post.next
    mid.next = pre
    aft_head = ListNode(0, mid)
    return aft_head 

## test
l = [1, 3, 5, 7, 9]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next
aft_head = reverse_list(head)
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next