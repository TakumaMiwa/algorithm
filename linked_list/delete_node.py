def delete_node(node):
    ## can be implemented in O(1),
    ## but ignoring the case in which node is tail 
    node.data = node.next.data
    node.next = node.next.next