packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5


def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names) # alice jane peter


def my_function(x, y, z):
    print(x, y, z)
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3

# unpacking
# 패킹된 값을 다시 unpacking하여 변수에 할당
# 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5

# * 활용한 언패킹
# *는 리스트의 요소를 언패킹하여 인자로 전달
def my_function(a, b, c):
    print(a, b, c)

name = ['Alice', 'Bob', 'Charlie']
my_function(*name)  # Alice Bob Charlie

# ** 활용한 언패킹
# **는 딕셔너리의 키-값 쌍을 언패킹하여 인자로 전달
def my_function(x, y, z):
    print(z, x, y) 

my_dict = {'x': 10, 'y': 20, 'z': 30}
my_function(**my_dict)  # 30 10 20