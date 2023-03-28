def reconstruct(traversal):
    if not traversal: return None
    elif len(traversal)==1: return BinaryTreeNode(data=traversal[0])
    def supporter(left, right):
        if left==right: return BinaryTreeNode(data=traversal[left])
        mid = left
        left += 1
        while traversal[left] < traversal[mid]: left += 1
        if mid+1==left: left_subtree = None
        else: left_subtree = supporter(mid+1, left-1)
        if right < left: right_subtree = None
        else: right_subtree = supporter(left, right)
        return BinaryTreeNode(data=traversal[mid], left=left_subtree, right=right_subtree)
    return supporter(0, len(traversal)-1)

def reconstruct(traversal):
    if not traversal: return None

    transition_point = next((i for i, a in enumerate(traversal) if a > traversal[0]), len(traversal))

    return BinaryTreeNode(traversal[0], reconstruct(traversal[1:transition_point]), reconstruct(traversal[transition_point:]))

def preorder_traversal(root):
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        if not node: continue
        
        result.append(node)
        stack.append(node.right)
        stack.append(node.left)
    return result
    
##test
from binarytree import BinaryTreeNode
preorder = [19, 7, 3, 2, 5, 11, 17, 13, 43, 23, 37, 29, 31, 41, 47, 53]

root = reconstruct(preorder)
print([x.data for x in preorder_traversal(root)])


