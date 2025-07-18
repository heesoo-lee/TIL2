# personality.py
# 질문, 성격 판별, 멘트 관리 함수



from data import QUESTIONS, PERSONALITY_TYPES, ADVICE_DICT

def ask_questions():
    """
    10개의 질문을 출력하고, 사용자로부터 '네' 또는 '아니오' 답변을 리스트로 수집
    대소문자, 공백 등 다양한 입력 허용
    """
    answers = []
    for q in QUESTIONS:
        while True:
            ans = input(f"{q['text']} (네/아니오): ").strip().replace(" ", "").lower()
            if ans in ("네", "예", "yes"):
                answers.append("네")
                break
            elif ans in ("아니오", "아니요", "no"):
                answers.append("아니오")
                break
            else:
                print("'네' 또는 '아니오'로만 답해주세요.")
    return answers

def analyze_personality(answers):
    """
    답변 리스트(10개)를 받아 각 성격유형별 점수를 누적, 최고점 유형 반환
    """
    scores = {ptype: 0 for ptype in PERSONALITY_TYPES}
    for idx, ans in enumerate(answers):
        if ans == "네":
            for ptype, weight in QUESTIONS[idx]["weights"].items():
                scores[ptype] += weight
    # 동점일 경우 여러 개 중 첫 번째 반환
    best_type = max(scores, key=lambda k: scores[k])
    return best_type

def get_advice(personality, concern=None):
    """
    성격 유형에 맞는 팩폭 멘트 반환
    """
    return ADVICE_DICT.get(personality, "스스로를 더 잘 이해하려고 노력해봐.")
