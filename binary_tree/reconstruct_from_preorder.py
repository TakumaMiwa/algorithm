from binarytree import BinaryTreeNode
from collections import namedtuple
def reconstruct(seq):
    NodeWithIndex = namedtuple('NodeWithTuple', ('node', 'idx'))
    def dfs(node, idx):
        if len(seq)-1<=idx: return NodeWithIndex(None, idx)
        if seq[idx+1]:
            node.left = BinaryTreeNode(data=seq[idx+1])
            right_idx = dfs(node.left, idx+1).idx
        else:
            right_idx = idx + 2
        
        if right_idx < len(seq) and seq[right_idx] is not None:
            node.right = BinaryTreeNode(data=seq[right_idx])
            next_idx = dfs(node.right, right_idx).idx
        else:
            next_idx = right_idx + 1
        return NodeWithIndex(node, next_idx)
    
    return dfs(BinaryTreeNode(data=seq[0]), 0).node

def reconstruct_preorder(preorder):
    def reconstruct_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None: return None

        left_subtree = reconstruct_helper(preorder_iter)
        right_subtree = reconstruct_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_helper(iter(preorder))


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

## test
seq = [314, 6, 271, 28, None, None, 0, None, None, 561, None, 3, 17, None, None, None, 6, 2, None, 1, 401, None, 641, None, None, 257, None, None, 271, None, 28, None, None]

n1 = reconstruct(seq)

print([x.data for x in inorder_traversal(n1)])


    


