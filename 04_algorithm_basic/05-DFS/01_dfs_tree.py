
tree = {'A' : ['B', 'C', 'D'],
        'B' : ['E', 'F'],
        'D' : ['G', 'H', 'I']}

def dfs(tree, node) :

    print(node)

    if node not in tree :
        return

    for child in tree[node] :
        dfs(tree, child)

dfs(tree, 'A')
