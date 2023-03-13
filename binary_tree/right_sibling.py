def right_sibling(root):
    def supporter(node):
        parent = node
        while parent:
            parent.left.next = parent.right
            parent.right.next = parent.next and parent.next.left
            parent = parent.next
    node = root
    while node and node.left:
        supporter(node)
        node = node.left
    return root

## test
from binarytree import BinaryTreeNode

n1 = BinaryTreeNode(data=314)
n2 = BinaryTreeNode(data=6)
n3 = BinaryTreeNode(data=6)
n4 = BinaryTreeNode(data=271)
n5 = BinaryTreeNode(data=561)
n6 = BinaryTreeNode(data=2)
n7 = BinaryTreeNode(data=271)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
root = right_sibling(n1)
while root:
    node = root
    l = []
    while node:
        l.append(node.data)
        node = node.next
    print(l)
    root = root.left
        


