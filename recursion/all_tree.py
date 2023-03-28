class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.next = next

def all_tree(n):
    if n==0: return [None]

    result = []
    for left_num in range(n):
        right_num = n - left_num - 1
        left_subtree = all_tree(left_num)
        right_subtree = all_tree(right_num)
        result += [BinaryTreeNode(0, left, right) for left in left_subtree for right in right_subtree]
    return result

            
