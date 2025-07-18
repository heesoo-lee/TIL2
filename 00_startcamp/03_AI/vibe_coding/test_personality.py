# test_personality.py
# personality.py의 주요 함수에 대한 간단한 테스트 코드

from personality import analyze_personality, get_advice

def test_analyze_personality():
    assert analyze_personality(["네", "아니오", "아니오"]) == "게으름"
    assert analyze_personality(["아니오", "네", "아니오"]) == "이성적"
    assert analyze_personality(["아니오", "아니오", "네"]) == "완벽주의자"
    assert analyze_personality(["아니오", "아니오", "아니오"]) == "감성적"

def test_get_advice():
    assert get_advice("게으름", "공부가 하기 싫어요").startswith("공부가 싫은 게 아니라")
    assert get_advice("이성적", "감정이 힘들어요").startswith("고민을 논리적으로")
    assert get_advice("완벽주의자", "일이 많아요").startswith("일이 많아서 힘든 게 아니라")
    assert get_advice("감성적", "마음이 복잡해요").startswith("감정에 너무 휘둘리지 말고")
    assert get_advice("기타", "모르겠어요").startswith("스스로를 더 잘 이해하려고")

if __name__ == "__main__":
    test_analyze_personality()
    test_get_advice()
    print("모든 테스트 통과!")
