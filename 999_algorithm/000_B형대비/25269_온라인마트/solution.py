'''
상품 : ID(PK), 품목, 제조사, 가격 정보
품목, 제조사 : 1 ~ 5 정수

상품 판매, 판매 종료 가능

같은 품목, 같은 제조사 상품들에 대해 특정 금액 가격 할인 가능
할인으로 가격이 0 or 음수가 된 상품은 판매 종료

사용자에게 특정 조건 만족 상품에 대해 가격 낮은 순으로 최대 5개 상품 검색 노출
조건 : 전체 상품, 특정 품목, 특정 제조사
가격 같은 경우, 상품 ID 오름차순
'''
import heapq


class RESULT:
    def __init__(self):
        self.cnt = 0
        self.IDs = [0] * 5

items = {} # mID -> (c, k, base, alive)
# 그룹별 alive 집합, base-price 힙, lazy 할인액
alives_ids = {(c, k): set() for c in range(1, 6) for k in range(1, 6)}
minheap = {(c, k): [] for c in range(1, 6) for k in range(1, 6)}
lazy = {(c,k): 0 for c in range(1, 6) for k in range(1, 6)}

def _pop_next_candidate(c, k, popbuf):
    '''
    (c, k) 그룹 힙에서 '살아있는 (top 기준)' 다음 후보 1개를 꺼내
    (eff_price, mID)를 반환하고, 힙에서 꺼낸 (base, mID)는  popbuf에 저장
    후보가 더 없으면 None 반환
    죽은 항목 or 현재가 <= 0 항목 건너뜀
    '''
    h = minheap[(c, k)]
    l = lazy[(c, k)]
    while h:
        base, mID = heapq.heappop(h)
        info = items.get(mID)

        # 죽었거나 그룹 불일치면 폐기
        if (info is None) or (not info['alive']) or info['c'] != c or info['k'] != k:
            continue

        # 현재가 <= 0 이면 즉시 종료 처리
        if base - l <= 0:
            info['alive'] = False
            alives_ids[(c, k)].discard(mID)
            continue

        # 유효 후보
        popbuf.append((base, mID)) # 나중에 힙 복원을 위해 저장
        return (base - l, mID)
    return None

def _cleanup_group_zero_price(c, k):
    '''
    (c, k) 그룹에 대해 lazy가 증가된 뒤,
    base - lazy <= 0이 된 상품을 힙에서 확인하며 제거
    힙에는 dead 항목도 남아있을 수 있으므로 skip 처리
    '''
    h = minheap[(c, k)]
    l = lazy[(c, k)]
    alive = alives_ids[(c, k)]

    while h:
        base, mID = h[0]
        # 이미 판매 종료된 상품이면 pop만 하고 continue
        info = items.get(mID)
        if (info is None) or (not info["alive"]):
            heapq.heappop(h)
            continue

        # 아직 같은 그룹에 속하는지 확인
        if info['c'] != c or info['k'] != k:
            heapq.heappop(h)
            continue

        if base - l <= 0:
            heapq.heappop(h)

            # alive면 종료 처리
            if info['alive']:
                info['alive'] = False
                if mID in alive:
                    alive.discard(mID)
        else:
            break

# ---------------------------------------------------------------------------------

def init() -> None:
    '''
    테스트 케이스에 대한 초기화 함수, 각 테케의 맨 처음 1회 호출
    초기에 판매되는 상품은 없음
    '''
    items.clear()
    for c in range(1, 6):
        for k in range(1, 6):
            alives_ids[(c, k)].clear()
            minheap[(c, k)].clear()
            lazy[(c, k)] = 0

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    '''
    ID == mID and 품목 == mCategory and 제조사 == mPrice -> 상품 판매 시작
    판매 시작 후, 품목 == mCategory and 제조사 == mPrice and 판매 중 -> 상품 개수 반환
    매개변수 mID는 중복값 아님 보장

    return : 같은 품목과 제조사를 가진 판매 중인 상품의 개수
    '''
    items[mID] = {"c": mCategory, "k": mCompany, "base": mPrice, "alive": True}
    l = lazy[(mCategory, mCompany)]

    # 현재가 <=0 -> 즉시 종료 (집합/ 힙에 넣지 않음)
    if mPrice - l <= 0:
        items[mID]["alive"] = False
        return len(alives_ids[(mCategory, mCompany)])
    alives_ids[(mCategory, mCompany)].add(mID)
    heapq.heappush(minheap[mCategory, mCompany], (mPrice, mID))

    return len(alives_ids[(mCategory, mCompany)])

def closeSale(mID : int) -> int:
    '''
    ID == mID -> 상품 판매 종료

    return : 판매 종료시 상품 가격, 판매 안하는 경우 -1
    '''
    info = items.get(mID)
    if not info or not info["alive"]:
        return -1
    c, k = info['c'], info['k']
    price = info["base"] - lazy[(c, k)]
    info["alive"] = False
    alives_ids[(c, k)].discard(mID)
    return price

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    '''
    품목 == mCategory and 제조사 == mCompany -> 가격 =- mAmount
    가격 <= 0 -> 상품 판매 종료

    return : 품목 == mCategory and 제조사 == mCompany and 판매중 -> 가격 개수
    '''
    key = (mCategory, mCompany)
    lazy[key] += mAmount
    _cleanup_group_zero_price(mCategory, mCompany) # 가격이 0 이하로 내려간 상품 정리
    return len(alives_ids[key])

def show(mHow : int, mCode : int):
    '''
    mHow == 0 -> 모든 상품
    mHow == 1 -> 품목 == mCode인 모든 상품
    mHow == 2 -> 제조사 == mCode인 모든 상품
    에 대해서 가격 낮은 순 최대 5개 상품 RESULT에 저장 & 반환
    가격 같은 경우 ID 오름차순
    판매 종료된 상품 제외

    반환 시,
    RESULT.cnt = 저장된 상품 개수
    RESULT.ID[i - 1] = i번째 상품 ID
    '''
    res = RESULT()

    # 대상 그룹 목록 구성
    groups = []
    if mHow == 0:
        groups = [(c, k) for c in range(1, 6) for k in range(1, 6)]
    elif mHow == 1:
        c = mCode
        groups = [(c, k) for k in range(1, 6)]
    else:
        k = mCode
        groups = [(c, k) for c in range(1, 6)]

    popped = { (c, k): [] for (c, k) in groups}

    # 각 그룹에서 첫 후보만 뽑아 전역 프론티어 힙 구성
    frontier = []
    for (c, k) in groups:
        # 혹시 남아 있을 수 있는 0원 이하 항목 정리(상단만 봄)
        _cleanup_group_zero_price(c, k)
        cand = _pop_next_candidate(c, k, popped[(c, k)])
        if cand is not None:
            eff, nid = cand
            heapq.heappush(frontier, (eff, nid, c, k))

    # 전역에서 최대 5개 추출
    out = []
    while frontier and len(out) < 5:
        eff, mID, c, k = heapq.heappop(frontier)
        out.append(mID)

        cand = _pop_next_candidate(c, k, popped[(c, k)])
        if cand is not None:
            neff, nid = cand
            heapq.heappush(frontier, (neff, nid, c, k))

    # 힙 복원
    for (c, k), arr in popped.items():
        h = minheap[(c, k)]
        for base, mID in arr:
            heapq.heappush(h, (base, mID))

    # 결과 채우기
    res.cnt = len(out)
    for i, mID in enumerate(out):
        res.IDs[i] = mID
    return res
