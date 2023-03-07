def even_odd_merge(head):
    p = head.next
    even_head, odd_head = ListNode(), ListNode()
    even, odd = even_head, odd_head
    while p:
        odd.next = p
        odd = odd.next
        if p.next:
            even.next = p.next
            even = even.next
            p = p.next.next
        else:
            break

    even.next = odd_head.next
    odd.next = None ## loop occurs if forgetting this 
    return even_head



## test
from listnode import ListNode 
l = [1, 2, 3, 4, 5, 6]
head = ListNode()
p = head
for num in l:
    p.next = ListNode(num, None)
    p = p.next

aft_head = even_odd_merge(head).next
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next