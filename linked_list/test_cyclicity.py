from listnode import ListNode
def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            start = start.next
            step += 1
            if start is end: return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next
        if fast is slow:
            p = head
            for _ in range(cycle_len(fast)):
                p = p.next

            it = head
            while it is not p:
                p, it = p.next, it.next

            return it
    return None

## test
n1 = ListNode(1, None)
n2 = ListNode(3, None)
n3 = ListNode(5, None)
n4 = ListNode(7, None)
n5 = ListNode(9, None)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3
head = ListNode(0, n1)

print(has_cycle(head).data)
