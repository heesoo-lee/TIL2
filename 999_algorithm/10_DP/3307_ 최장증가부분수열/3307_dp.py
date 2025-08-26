t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    dp = {}
    answer = 0

    for x in nums:
        dp[x] = dp.get(x-1, 0) + 1
        if dp[x] > answer:
            answer = dp[x]

    print(answer)