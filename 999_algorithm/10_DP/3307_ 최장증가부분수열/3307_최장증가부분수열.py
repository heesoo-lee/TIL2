t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    memo = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] <= nums[i]:
                memo[i] = max(memo[i], memo[j] + 1)

    print(f'#{tc} {max(memo)}')
