# 인스턴스 메서드
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')
person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.


# 클래스 메서드
# 클래스가 호출하는 메서드
# 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
# 호출 시 첫번째 인자로 해당 메서드 호출하는 클래스(cls) 전달됨
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod  # 데코레이터
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS')



# 정적 메서드
# 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
# 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
# 호출 시 작성해야 할 매개변수가 없음
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'
reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # dlrow ,olleh
capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)  # Hello, world



# 클래스 정의하면 클래스와 해당하는 이름 공간 생성
# 인스턴스 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
# 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색



# 매직 메서드
# 인스턴스 메서드
# 특정 상황에 자동으로 호출 되는 메서드
# Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
# 스페셜 매서드 혹은 매직 메서드라 불림
# 예 : __str__(self), __len__(self), __lt__(self, other), __le__(self, other), 
# __eq__(self, other), __gt__(self, other), __ge__(self, other), __ne__(self, other)