# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 
# 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형

# Sequence Type
# 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
# str, list, tuple, range

bugs = 'roaches'
counts = 13
area = 'living room'
# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll
print(my_str[:3]) # hel
print(my_str[2:]) # llo
print(my_str[-1]) # o
print(my_str[-2:]) # lo
print(my_str[-3:-1]) # ll
print(my_str[1:4:2]) # el
print(my_str[::2]) # hlo
print(my_str[::-1]) # olleh
# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'


# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!

# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split
text = 'Hello, world!'
words = text.split(',')
print(words)  # ['Hello', ' world!']

# join
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'
