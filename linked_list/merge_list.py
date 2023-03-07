from listnode import ListNode
def merge_list(p1, p2):
    head = ListNode(0, None)
    p = head
    while p1 and p2:
        if p1.data < p2.data:
            p.next = p1
            p, p1 = p.next, p1.next
        else:
            p.next = p2
            p, p2 = p.next, p2.next
    p.next = p1 if p1 else p2

    return head.next

## test
l1 = [2, 5, 7]
l2 = [3, 11]

head1, head2 = ListNode(0, None), ListNode(0, None)
p1, p2 = head1, head2
for num in l1:
    p1.next = ListNode(num, None)
    p1 = p1.next
for num in l2:
    p2.next = ListNode(num, None)
    p2 = p2.next

aft_head = merge_list(head1.next, head2.next)
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next

    

