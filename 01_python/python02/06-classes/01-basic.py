# 클래스 정의
class Person:
    blood_color = 'red'
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)


# 객체 정리
# 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
# 속성(attribute) : 어떤 상태(데이터)를 가지는가?
# 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
# 객체(object) = 속성(attribute) + 기능(method)

# 생성자 함수
# 객체를 생성할 때 자동으로 호출되는 특별한 메서드
# __init__ 메서드로 정의
# 객체 초기화 담당
# 생성자 함수 통해 인스턴스를 생성하고 필요한 초기값 설정