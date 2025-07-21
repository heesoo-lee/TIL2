packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)


numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


def my_func(*objects):
    print (objects) # (1, 2, 3, 4, 5)
    print(type(objects)) # <class 'tuple'>
my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>

# packing
# 여러 개의 값을 하나의 변수에 묶어서 담는 것
# 변수에 담긴 값들은 tuple 형태로 묶임
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

# * 활용한 패킹
# *b는 남은 요소들을 리스트로 패킹하여 할당
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

