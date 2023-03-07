def has_overlapping(head1, head2):
    l1 = l2 = 0
    p1, p2 = head1, head2
    while p1:
        l1, p1 = l1+1, p1.next
    while p2:
        l2, p2 = l2+1, p2.next
    if l2 < l1:
        p1, p2 = head2, head1
        l1, l2 = l2, l1
    else:
        p1, p2 = head1, head2
    for _ in range(l2 - l1):
        p2 = p2.next
    
    while p1 and p2 and p1 != p2:
        p1, p2 = p1.next, p2.next
    return p1


## test

from listnode import ListNode
n1 = ListNode(1, None)
n2 = ListNode(3, None)
n3 = ListNode(5, None)
n4 = ListNode(7, None)
n5 = ListNode(9, None)
n1.next = n2
n2.next = n3
n3.next = n5
n4.next = n5
head1 = ListNode(0, n1)
head2 = ListNode(0, n4)
print(has_overlapping(head1,head2).data)
