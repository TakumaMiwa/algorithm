def exterior(root):
    def is_leaf(node):
        return not node.left and not node.right
    
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return(([subtree] if is_boundary or is_leaf(subtree) else []) + 
               left_boundary_and_leaves(subtree.left, is_boundary) + 
               left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree: return []
        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) + 
               right_boundary_and_leaves(subtree.right, is_boundary) +
               ([subtree] if is_boundary or is_leaf(subtree) else []))
    return ([root] + left_boundary_and_leaves(root.left, True) +
            right_boundary_and_leaves(root.right, True))

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

print([x.data for x in exterior(n1)])