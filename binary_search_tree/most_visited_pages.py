from bintrees import RBTree
from collections import defaultdict
def most_visited_pages(l, k):
    dic = defaultdict(int)
    tree = RBTree()

    for page in l:
        dic[page] += 1
        if len(list(dic.keys())) <= k and page not in tree:
            tree.insert(dic[page], page)
        elif page in tree:
            tree.discard(page)
            tree.insert(dic[page], page)
        elif tree.min_key() < dic[page]:
            tree.pop_min()
            tree.insert(dic[page], page)

## test
pages = [1, 2, 3, 3, 2, 2, 2, 1, 3, 4, 3, 2, 3]
most_visited_pages(pages, 2)


    
        

    
