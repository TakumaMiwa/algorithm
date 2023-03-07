def add_list_base(head1, head2):
    p1, p2 = head1.next, head2.next
    s, c = 0, 0
    dummy_head = ListNode()
    p = dummy_head
    while p1 or p2 or c:
        p1_num = p1.data if p1 else 0
        p2_num = p2.data if p2 else 0
        s = p1_num + p2_num + c
        c = s // 10
        s %= 10
        p.next = ListNode(s, None)
        p, p1, p2 = p.next, p1.next if p1 else None, p2.next if p2 else None
    return dummy_head
## test
from listnode import ListNode 
l1 = [3, 1, 4]
l2 = [7, 0, 9]
head1 = ListNode()
p = head1
for num in l1:
    p.next = ListNode(num, None)
    p = p.next

head2 = ListNode()
p = head2
for num in l2:
    p.next = ListNode(num, None)
    p = p.next

aft_head = add_list_base(head1, head2).next
while aft_head:
    print(aft_head.data)
    aft_head = aft_head.next