t = int(input())
for test in range(1, t+1) :
    n = int(input())

    tree = [0] * (n+1)
    order = []

    def traversal(idx) :
        if idx <= n :
            traversal(idx*2)
            order.append(idx)
            traversal(idx*2 + 1)

    traversal(1)
    for value, index in enumerate(order) :
        tree[index] = value+1

    print(f"#{test}", tree[1], tree[n//2])