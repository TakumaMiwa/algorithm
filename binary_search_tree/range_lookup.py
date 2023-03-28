def range_lookup(tree, lookup_range):
    result = []
    low, high = lookup_range
    def dfs(node):
        if not node: return
        if low <= node.data <= high:
            dfs(node.left)
            result.append(node.data)
            dfs(node.right)
        elif node.data < low:
            dfs(node.right)
        else:
            dfs(node.left)
    dfs(tree)
    return result

## test
from binarytree import BinaryTreeNode

n1 = BinaryTreeNode(data=19)
n2 = BinaryTreeNode(data=7)
n3 = BinaryTreeNode(data=43)
n4 = BinaryTreeNode(data=3)
n5 = BinaryTreeNode(data=11)
n6 = BinaryTreeNode(data=23)
n7 = BinaryTreeNode(data=47)
n8 = BinaryTreeNode(data=2)
n9 = BinaryTreeNode(data=5)
n10 = BinaryTreeNode(data=17)
n11 = BinaryTreeNode(data=37)
n12 = BinaryTreeNode(data=53)
n13 = BinaryTreeNode(data=13)
n14 = BinaryTreeNode(data=29)
n15 = BinaryTreeNode(data=41)
n16 = BinaryTreeNode(data=31)
n1.left = n2
n1.right = n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.left, n4.right = n8, n9
n5.right = n10
n6.right = n11
n7.right = n12
n10.left = n13 
n11.left, n11.right = n14, n15
n14.right = n16

print(range_lookup(n1, [16, 31]))