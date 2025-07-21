# Set
# 순서와 중복이 없는 변경 가능한 자료형
# 수학에서의 집합과 동일한 연산 처리 가능
# 중괄호 {}로 표기

my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}
print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}


my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}
# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}
# 교집합
print(my_set_1 & my_set_2)  # {3}


# add
# 이미 x가 존재하면 아무런 변화 없음
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)  # {'b', 2, 3, 1, 4, 'c', 'a'}
my_set.add(4)
print(my_set)  # {'b', 2, 3, 1, 4, 'c', 'a'}


# remove
# x가 존재하지 않으면 KeyError 발생
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)  # {'b', 3, 1, 'c', 'a'}
my_set.remove(10) # KeyError
print(my_set)  # {'b', 3, 1, 'c', 'a'}
