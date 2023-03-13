from binarytree import BinaryTreeNode
def reconstruct_tree(preorder, inorder):
    node_to_inorder_idx = {x: i for i, x in enumerate(inorder)}
    def supporter(pre_start, pre_end, in_start, in_end):
        if pre_end <= pre_start or in_end <= in_start: return None
        
        root_idx = node_to_inorder_idx[preorder[pre_start]]
        print(inorder[root_idx])
        left_subtree_size = root_idx - in_start

        return BinaryTreeNode(preorder[pre_start], 
                              supporter(pre_start+1, pre_start+1+left_subtree_size, in_start, root_idx),
                              supporter(pre_start+1+left_subtree_size, pre_end, root_idx+1, in_end))
    
    return supporter(0, len(preorder), 0, len(inorder))

## test
def inorder_traversal(root):
    stack = [root]
    result = []
    dic = set()
    while stack:
        node = stack.pop()
        if not node: continue
        if node in dic:
            result.append(node)
            continue
        dic.add(node)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)
    return result

preorder = [314, 6, 271, 28, 0, 561, 3, 17, 7, 2, 1, 401, 641, 257, 272, 29]
inorder = [28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 7, 272, 29]

root = reconstruct_tree(preorder, inorder)
print([x.data for x in inorder_traversal(root)])
