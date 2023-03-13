def leaf_linkedlist(root):
    result = []
    def dfs(node):
        if not node.left and not node.right:
            result.append(node.data)
            return
        if node.left: dfs(node.left)
        if node.right: dfs(node.right)
    dfs(root)
    return result
def leaf_linkedlist(root):
    if not root: return []
    elif not root.left and not root.right: return [root]
    else:
        return leaf_linkedlist(root.left) + leaf_linkedlist(root.right)
from binarytree import BinaryTreeNode
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

print(leaf_linkedlist(n1))