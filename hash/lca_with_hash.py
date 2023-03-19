class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.next = next

def lca(node1, node2):
    dic = set()
    while node1 and node2:
        if node1 in dic: return node1
        elif node2 in dic: return node2

        dic.add(node1)
        dic.add(node2)

        if node1: node1 = node1.parent
        if node2: node2 = node2.parent

## test
n1 = BinaryTreeNode(data=314)
n2 = BinaryTreeNode(data=6)
n3 = BinaryTreeNode(data=6)
n4 = BinaryTreeNode(data=271)
n5 = BinaryTreeNode(data=561)
n6 = BinaryTreeNode(data=2)
n7 = BinaryTreeNode(data=271)
n8 = BinaryTreeNode(data=28)
n9 = BinaryTreeNode(data=0)
n10 = BinaryTreeNode(data=3)
n11 = BinaryTreeNode(data=1)
n12 = BinaryTreeNode(data=28)
n13 = BinaryTreeNode(data=17)
n14 = BinaryTreeNode(data=401)
n15 = BinaryTreeNode(data=257)
n16 = BinaryTreeNode(data=641)
n1.left = n2
n2.parent = n1
n1.right = n3
n3.parent = n1
n2.left, n2.right = n4, n5
n4.parent = n5.parent = n2
n3.left, n3.right = n6, n7
n6.parent = n7.parent = n3
n4.left, n4.right = n8, n9
n8.parent = n9.parent = n4
n5.right = n10
n10.parent = n5
n6.right = n11
n11.parent = n6
n7.right = n12
n12.parent = n7
n10.left = n13 
n13.parent = n10
n11.left, n11.right = n14, n15
n14.parent = n15.parent = n11
n14.right = n16
n16.parent = n14

print(lca(n4, n10).data)
