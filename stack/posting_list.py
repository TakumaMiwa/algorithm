class ListNode:
    def __init__(self, data=0, next_node=None, jump_node = None):
        self.data = data
        self.next = next_node
        self.jump = jump_node

def posting_list(head):
    result = []
    p = head.next
    while p:
        if p in result:
            p = p.next
            continue
        result.append(p)
        if p.jump and p.jump not in result:
            stack = [p.jump]
            while stack:
                node = stack.pop()
                result.append(node)
                if node.jump and node.jump not in result:
                    stack.append(node.jump)
        p = p.next
    return result

## test

n4 = ListNode(4, None, None)
n3 = ListNode(3, n4, )
n2 = ListNode(2, n3, None)
n1 = ListNode(1, n2, None)

n4.jump = n4
n3.jump = n2
n2.jump = n4
n1.jump = n3

head = ListNode(0, n1)

print(list(map(lambda x: x.data, posting_list(head))))
