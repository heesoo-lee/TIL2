n = int(input())
row = list(map(int, input().split()))
up_count = 0
down_count = 0

count = 1
for i in range(1, n) :
    if row[i-1] <= row[i] :
        count += 1
        up_count = max(up_count, count)
    else :
        count = 1

count = 1
for i in range(1, n) :
    if row[i-1] >= row[i] :
        count += 1
        down_count = max(down_count, count)
    else :
        count = 1

print(max(up_count, down_count))