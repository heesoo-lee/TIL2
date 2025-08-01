def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        remain: 선택되지 않고 남은 값 목록
    '''
    if not remain :
        print(selected)
    else :
        for idx in range(len(remain)) :
            select_item = remain[idx]
            remain_list = remain[:idx-1] + remain[i+1:]
            perm(selected + [select_item], remain_list)

# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
