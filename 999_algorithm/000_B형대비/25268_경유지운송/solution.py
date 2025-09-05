# n개의 도시 (ID 값 : 0 ~ n-1)
# 운송 가능한 최대 중량, 경유지 3개

info = []

def init(N, K, sCity, eCity, mLimit):
	for i in range(K):
		info.append((mLimit, sCity, eCity))


def add(sCity, eCity, mLimit):
	info.append(mLimit, sCity, eCity)


def calculate(sCity, eCity, M, mStopover):
    return
