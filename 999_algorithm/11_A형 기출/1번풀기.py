t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    max_sum = -10000 * n

    for i in range(n - 2 * k + 1):
        j = 0
        a = sum(nums[i: i + k])
        while i + 2 * k + j <= n:
            max_sum = max(max_sum, a + sum(nums[i + k + j: i + 2 * k + j]))
            j += 1

    print(f'#{tc} {max_sum}')
