t = int(input())
for tc in range(1, t+1):
    N, a, b = map(int, input().split())

    def bino(n, k):
        dp = [[0 for _ in range(k + 1)] for _  in range(n + 1)]

        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n][k]

    result = bino(N, a)
    print(f'#{tc} {result}')