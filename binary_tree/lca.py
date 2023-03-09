from binarytree import BinaryTreeNode
from collections import namedtuple
def lca(tree, node1, node2):
    NodeState = namedtuple('NodeState', ('node1', 'node2', 'lca'))

    def dfs(root):
        if not root: return NodeState(False, False, None)

        left_state = dfs(root.left)
        if left_state.lca: return NodeState(True, True, left_state.lca)

        right_state = dfs(root.right)
        if right_state.lca: return NodeState(True, True, right_state.lca)

        if (left_state.node1 and right_state.node2) or (left_state.node2 and right_state.node1) or (root==node1 and (left_state.node2 or right_state.node2)) or (root==node2 and (left_state.node1 or right_state.node1)):
            return NodeState(True, True, root)
        
        return NodeState(left_state.node1 or right_state.node1 or root==node1,
                left_state.node2 or right_state.node2 or root==node2,
                None)
    
    return dfs(tree).lca.data



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

print(lca(n1, n4, n10))

        