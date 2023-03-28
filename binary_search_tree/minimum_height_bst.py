from binarytree import BinaryTreeNode
def min_height_bst(sorted_array):
    def supporter(left, right):
        if left == right: return BinaryTreeNode(sorted_array[left])
        mid = (left + right) // 2
        return BinaryTreeNode(sorted_array[mid], supporter(left, mid-1), supporter(mid+1, right))
    return supporter(0, len(sorted_array)-1)

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

l = [1, 2, 3, 4, 5, 6, 7]
print([x.data for x in inorder_traversal(min_height_bst(l))])
