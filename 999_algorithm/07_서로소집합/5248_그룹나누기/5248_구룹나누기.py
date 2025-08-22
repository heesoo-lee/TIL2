t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))

    groups = [[i] for i in range(1, n+1)]

    for i in range(0, m*2, 2):
        for j in range(len(groups)):
            if info[i] in groups[j]:
                groups[j] += groups[info[i+1] - 1]
                groups[info[i+1] - 1].clear()

    count = 0
    for group in groups:
        if len(group) > 0:
            count += 1

    print(f'#{tc} {count}')
