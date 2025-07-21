my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}

# key는 불변 자료형만 사용 가능 (str, int, tuple, range 등)
# value는 모든 자료형 사용 가능

my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict['apple'])  # 12
print(my_dict['list'])  # [1, 2, 3]
# 추가
my_dict['banana'] = 50
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}
# 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}

# 대괄호 접근법
print(my_dict['apple'])  # 100
print(my_dict['orange'])  # KeyError

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country'))  # None
print(person.get('country', 'Unknown'))  # Unknown

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age’])
for k in person.keys():
    print(k)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values ([‘Alice’, 25])
for v in person.values():
    print(v)


# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

for k, v in person.items():
    print(k, v)


# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
print(person.pop('country'))  # KeyError


