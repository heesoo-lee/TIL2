# main.py
# 프로그램 실행 및 전체 흐름 제어

from personality import ask_questions, analyze_personality, get_advice

def main():
    print("\n=== 성격 분석 팩트 폭행 프로그램 ===\n")
    print("10개의 질문에 네/아니오로 답해주세요.\n")
    # Step 1: 질문 및 응답 수집
    answers = ask_questions()
    # Step 2: 성격 유형 판별
    personality = analyze_personality(answers)
    print(f"\n[분석 결과] 당신의 성격 유형은: {personality}\n")
    # Step 3: 고민 입력
    concern = input("고민이 있다면 입력하세요(엔터만 눌러도 진행): ")
    # Step 4: 팩폭 상담 멘트 출력
    print("[팩폭 상담]")
    print(get_advice(personality, concern))

if __name__ == "__main__":
    main()
