# data.py
# 질문, 성격유형, 멘트 데이터를 분리하여 관리

PERSONALITY_TYPES = [
    "완벽주의자",
    "게으름 대장",
    "감성 폭발러",
    "이성 만렙러",
    "자존감 낮은 타입",
    "자기애 최강자",
    "우유부단형",
    "의욕 과잉형",
    "현실 회피형",
    "타인 의존형"
]

QUESTIONS = [
    {
        "text": "일 할 땐 폴더랑 노션 정리는 완벽한데, 정작 시작은 안 함.",
        "weights": {"완벽주의자": 1.0, "우유부단형": 0.5}
    },
    {
        "text": "해야 하는 일 앞두고 갑자기 빨래 개고, 냉장고 정리까지 함.",
        "weights": {"게으름 대장": 1.0, "현실 회피형": 0.5}
    },
    {
        "text": "기분 안 좋을 땐 알람 울리자마자 그냥 하루 접고 싶다.",
        "weights": {"감성 폭발러": 1.0, "자존감 낮은 타입": 0.5}
    },
    {
        "text": "계획은 세웠고 문제점도 다 파악했는데, 시작은 내일부터임.",
        "weights": {"이성 만렙러": 1.0, "완벽주의자": 0.5}
    },
    {
        "text": "인스타보다가 친구들 잘 나가는 거 보면 '아 나는 뭐 하고 있지' 싶을 때 있다.",
        "weights": {"자존감 낮은 타입": 1.0, "타인 의존형": 0.5}
    },
    {
        "text": "솔직히 난 잘될 사람 같은데, 세상이 아직 몰라주는 중임.",
        "weights": {"자기애 최강자": 1.0, "의욕 과잉형": 0.5}
    },
    {
        "text": "메뉴 고를 때 10분 고민하다가 결국 ‘그냥 네가 시켜’ 했던 적 있다.",
        "weights": {"우유부단형": 1.0, "감성 폭발러": 0.5}
    },
    {
        "text": "플래너는 잘 샀는데, 그 플래너를 쓴 적은 별로 없음.",
        "weights": {"의욕 과잉형": 1.0, "게으름 대장": 0.5}
    },
    {
        "text": "하기 싫은 일 생기면 갑자기 청소하고, 드라마 정주행하고, 세상 진지해짐.",
        "weights": {"현실 회피형": 1.0, "감성 폭발러": 0.5}
    },
    {
        "text": "누가 툭 던진 말에 괜히 하루 종일 곱씹고, 괜찮은 척하다가 밤에 생각남.",
        "weights": {"타인 의존형": 1.0, "자존감 낮은 타입": 0.5}
    }
]

ADVICE_DICT = {
    "완벽주의자": "계획만 세우다 달력만 넘기지 말고, 너 달력 만드는 직업 아니잖아.\n완벽해질 때까지 기다리는 동안 남들은 이미 반쯤 가 있더라.",
    "게으름 대장": "할 일은 많다면서 침대랑 결혼이라도 했냐?\n‘내일 할게’가 쌓이면 결국 인생도 미루기만 하다 끝나.",
    "감성 폭발러": "네 기분 따라 움직이면 리모컨이냐?\n감정 팔이 그만하고 현실 좀 켜. 세상은 너한테 관심 없어.",
    "이성 만렙러": "계산은 박사인데 행동은 유치원생이네?\n그렇게 머리 굴려놓고 손은 왜 가만히 있어?",
    "자존감 낮은 타입": "누가 너 무시하는 줄 아냐? 아무도 관심 없어.\n네가 널 그렇게 만든 거야. 이제 좀 끌어올려.",
    "자기애 최강자": "넌 특별해, 네 머릿속에서만.\n근데 현실에선 아무도 몰라. 그게 문제야.",
    "우유부단형": "선택 못 하면 선택 당하는 인생 산다.\n계속 남 핑계 대면 진짜 네 인생은 남 손에 맡겨진다.",
    "의욕 과잉형": "시작할 땐 불꽃놀이인데 끝은 늘 꺼진 성냥이야.\n열정도 좋지만, 유지력이 없으면 그냥 소음이야.",
    "현실 회피형": "현실이 싫다고 눈 감으면, 깼을 땐 더 망가져 있어.\n그게 네가 피하고 싶어 했던 진짜 현실이야.",
    "타인 의존형": "결정은 못 하면서 남 탓은 빠르더라.\n그 인생 너 거 맞아? 아니면 네가 들고 있는 리모컨에 남이 앉아 있니?"
}
