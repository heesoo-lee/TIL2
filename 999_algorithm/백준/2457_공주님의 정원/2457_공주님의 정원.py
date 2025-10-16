n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
days = []

for day in info:
    a, b, c, d = day
    start = (a * 100) + b
    end = (c * 100) + d
    days.append((start, end))

flower_count = 0
mid_point = 0
end_point = 0

while end_point < 1130:
    yes = False
    if flower_count == 0:
        for day in days:
            s, e = day
            if s < 301:
                # print(s)
                if e > mid_point:
                    mid_point = e
                    # print(mid_point)
                    yes = True

    else:
        for day in days:
            s, e = day
            if s < mid_point:
                end_point = max(end_point, e)
                yes = True

    if yes:
        flower_count += 1
    else:
        print(0)
        break

if yes:
    print(flower_count)