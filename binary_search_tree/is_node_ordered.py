def is_node_ordered(node1, node2, middle):
    ## O(h); h is the height of tree
    target_nodes = [node1, node2]
    target_flag = [False, False]
    def dfs(node):
        if not node: return
        if node in target_nodes:
            node_idx = target_nodes.index(node)
            target_flag[node_idx] = True
        dfs(node.left)
        dfs(node.right)
    dfs(middle)
    if all(target_flag) or not any(target_flag): return False
    descendant_idx = target_flag.index(False)
    target = target_nodes[descendant_idx]
    def dfs(node):
        if not node: return False
        if node==middle: return True
        return dfs(node.left) or dfs(node.right)
    return dfs(target)

def is_node_ordered(node1, node2, middle):
    ## O(d); d is the difference between the heights of two nodes

    p1, p2 = node1, node2
    while (p1 is not node2 and p1 is not middle and
           p2 is not node1 and p2 is not middle and (p1 or p2)):
        if p1:
            p1 = p1.left if p1.data > middle.data else p1.right
        if p2:
            p2 = p2.left if p2.data > middle.data else p2.right

    if (p1 is not middle and p2 is not middle) or p1 is node2 or p2 is node1: return False

    def search_target(source, target):
        while source and source is not target:
            source = source.left if source.data > target.data else source.right
        
        return source is target

    return search_target(
        middle,
        node2 if p1 is middle else node1
    )
    


    


## test
from binarytree import BinaryTreeNode

n1 = BinaryTreeNode(data=19)
n2 = BinaryTreeNode(data=7)
n3 = BinaryTreeNode(data=43)
n4 = BinaryTreeNode(data=3)
n5 = BinaryTreeNode(data=11)
n6 = BinaryTreeNode(data=23)
n7 = BinaryTreeNode(data=47)
n8 = BinaryTreeNode(data=2)
n9 = BinaryTreeNode(data=5)
n10 = BinaryTreeNode(data=17)
n11 = BinaryTreeNode(data=37)
n12 = BinaryTreeNode(data=53)
n13 = BinaryTreeNode(data=13)
n14 = BinaryTreeNode(data=29)
n15 = BinaryTreeNode(data=41)
n16 = BinaryTreeNode(data=31)
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

print(is_node_ordered(n1, n10, n2))
