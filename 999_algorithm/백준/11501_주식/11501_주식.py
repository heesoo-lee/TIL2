t = int(input())

# -------- 시간 초과 -----------
# for _ in range(t):
#     n = int(input())
#     price = list(map(int, input().split()))
#     answer = 0
#
#     for i in range(n):
#         last = price[i:]
#         if last[0] == max(last):
#             continue
#         answer += (max(last) - last[0])
#
#     print(answer)


for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    answer = 0

    for i in range(n - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else :
            answer += (max_price - price[i])

    print(answer)
