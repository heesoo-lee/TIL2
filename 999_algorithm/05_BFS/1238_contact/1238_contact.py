from collections import deque

def bfs():
    visited =set()
    queue = deque([(s, 0)])
    visited.add(s)
    max_count = 0
    last = []

    while queue:
        caller, count = queue.popleft()

        if max_count < count :
            last = [caller]
            max_count = count

        elif max_count == count :
            last.append(caller)

        for next_caller in contact.get(caller) :
            if next_caller not in visited :
                visited.add(next_caller)
                queue.append((next_caller, count + 1))

    return max(last)

for tc in range(1, 11) :
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))
    contact = {i : [] for i in range(1, 101)}
    for i in range(0, n, 2) :
        contact[numbers[i]].append(numbers[i+1])
    
    answer = bfs()
    print(f'#{tc} {answer}')