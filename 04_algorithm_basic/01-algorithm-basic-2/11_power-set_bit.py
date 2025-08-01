arr = [1, 2, 3]
n = len(arr)
subsets = []

# for idx in range(2**n):
for idx in range(1 << n) :
    tmp_subset = []
    for j in range(n) : # j번째 요소가 이번 경우의 수에 사용되었는지 판별
        if idx & (1 << j) :
            tmp_subset.append(arr[j])
    if sum(tmp_subset) == 3 :
        subsets.append(tmp_subset)
print(subsets)
