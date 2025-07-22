class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()  # 반갑습니다. 박교수입니다.
# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()  # 반갑습니다. 김학생입니다.


# 다중 상속 예시
# 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
# 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY


# 상속
# MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록 생성
# 부모 클래스로부터 상속된 속성들의 검색을 C3 선형화 규칙에 맞춰 진행
# 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
# 속성이 D에서 발견되지 않으면 B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾는 순으로 진행
# class D(B,C) :
    # pass

# MRO 예시
O = object
class D(O) : pass
class E(O) : pass
class F(O) : pass
class B(D, E) : pass
class C(F, D) : pass
class A(B, C) : pass
# A 클래스의 상속 탐색 순서를 출력
print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, 
# <class '__main__.F'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>)