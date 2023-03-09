from binarytree import BinaryTreeNode

def is_symmetric(root):
    def check_subtree(root1, root2):
        if not root1 and not root2: return True
        elif root1 and root2:
            return root1.data==root2.data and check_subtree(root1.left, root2.right) and check_subtree(root1.right, root2.left)
        
        return False
    return check_subtree(root.left, root.right)

## test
n1 = BinaryTreeNode(data=314)
n2 = BinaryTreeNode(data=6)
n3 = BinaryTreeNode(data=6)
n4 = BinaryTreeNode(data=2)
n5 = BinaryTreeNode(data=2)
n6 = BinaryTreeNode(data=3)
n7 = BinaryTreeNode(data=3)
n1.left, n1.right = n2, n3
n2.right = n4
n3.left = n5
n4.right = n6
n5.left = n7
print(is_symmetric(n1))