t = int(input())
for test in range(1, t+1) :
    n, m, l = map(int, input().split())
    leafs = [list(map(int, input().split())) for _ in range(m)]

    tree = [0] * (n+1)

    for leaf in leafs :
        tree[leaf[0]] = leaf[1]

    for i in range(n, 0, -1) :
        if i * 2 <= n :
            if i * 2 + 1 <= n :
                tree[i] = tree[i*2+1] + tree[i*2]
            else :
                tree[i] = tree[i*2]

    print(f"#{test} {tree[l]}")

