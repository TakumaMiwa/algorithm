class TreeNode:
    def __init__(self, data=None, edges=[]):
        self.data = data
        self.edges = edges

def tree_diameter(root):
    max_distance = [0]
    def supporter(node):
        if not node.edges: return node.data
        child_distances = [supporter(child) for child in node.edges]
        child_distances.sort()
        if 2 <= len(child_distances):
            max_distance[0] = max(max_distance[0], sum(child_distances[-2:]))
        return max(child_distances)+node.data
    supporter(root)
    return max_distance[0]

## test
n1 = TreeNode(0, [])
n2 = TreeNode(7, [])
n3 = TreeNode(14, [])
n4 = TreeNode(3, [])
n5 = TreeNode(4, [])
n6 = TreeNode(3, [])
n7 = TreeNode(6, [])
n5.edges = [n7]
n2.edges = [n5, n6]
n1.edges = [n2, n3, n4]

print(tree_diameter(n1))



