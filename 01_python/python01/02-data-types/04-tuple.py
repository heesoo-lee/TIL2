# 튜플(Tuple)
# 튜플은 변경 불가능한 시퀀스 자료형
# 튜플은 소괄호로 정의하며, 요소는 변경할 수 없음
# 튜플은 리스트와 유사하지만, 요소를 변경할 수 없고, 해시 가능하여 딕셔너리의 키로 사용할 수 있음
# 튜플은 리스트보다 메모리 사용이 적고, 성능이 더 빠름
# 튜플은 여러 값을 묶어서 하나의 값으로 다룰 때 유용함

my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)


my_tuple = (1, 'a', 3, 'b', 5)
# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'


x, y = (10, 20)
print(x)  # 10
print(y)  # 20
# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
