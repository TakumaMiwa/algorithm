from binarytree import BinaryTreeNode
def sum_root_to_leaf(root):
    result = [0]
    def dfs(node, num):
        if not node:
            result[0] += num
            return 

        num = (num << 1) + node.data
        dfs(node.left, num)
        dfs(node.right, num)
        return 
    
    
    dfs(root, 0)
    return result[0]

## test
n1 = BinaryTreeNode(data=1)
n2 = BinaryTreeNode(data=0)
n3 = BinaryTreeNode(data=1)
n4 = BinaryTreeNode(data=0)
n5 = BinaryTreeNode(data=1)
n6 = BinaryTreeNode(data=0)
n7 = BinaryTreeNode(data=0)
n8 = BinaryTreeNode(data=0)
n9 = BinaryTreeNode(data=1)
n10 = BinaryTreeNode(data=1)
n11 = BinaryTreeNode(data=0)
n12 = BinaryTreeNode(data=0)
n13 = BinaryTreeNode(data=0)
n14 = BinaryTreeNode(data=1)
n15 = BinaryTreeNode(data=0)
n16 = BinaryTreeNode(data=1)
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

print(sum_root_to_leaf(n1))


