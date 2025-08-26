t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(m)]

    dp = [0] * (n + 1)

    for i in range(m):
        for w in range(n, item[i][0] -1, -1):
            dp[w] = max(dp[w], item[i][1] + dp[w - item[i][0]])

    answer = dp[n]
    print(f'#{tc} {answer}')
