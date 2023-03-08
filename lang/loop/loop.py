print("""
for loop
""")
for_loop = [1, 2, 3, 4, 5]

for item in for_loop:
    print(item)

print("""
while loop
""")
while_loop = [1, 2, 3, 4, 5]

i = 0
while i < len(while_loop):
    print(while_loop[i])
    i += 1

print("""
iterator
""")
iter_loop = [1, 2, 3, 4, 5]
iterator = iter(while_loop)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

enum_loop = [1, 2, 3, 4, 5]

print("""
enumerate()
반복 가능한 객체(리스트, 튜플, 문자열 등)를 입력으로 받아
인덱스와 해당 요소를 튜플로 반환합니다.
""")
for i, item in enumerate(enum_loop):
    print(i, item)

print("""
enumerate(iterable, start)
인덱스를 2부터 시작하도록 지정할 수 있습니다.
item은 2부터 시작하지 않습니다.
""")
for i, item in enumerate(enum_loop, 2):
    print(i, item)

print("""
zip()
여러 시퀀스(리스트, 튜플, 문자열 등)를 동시에 순회하는 방법
""")
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = ['a', 'b', 'c', 'd', 'e']

for item_1, item_2 in zip(my_list_1, my_list_2):
    print(item_1, item_2)

print("""
리스트 컴프리헨션: list comprehension
[표현식 for 항목 in 시퀀스 if 조건문]
""")
print("1부터 10까지의 숫자 중에서 짝수만 저장한 리스트를 만듭니다.")
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10]

print("리스트의 각 항목에 2를 곱한 결과를 저장한 리스트를 만듭니다.")
my_list = [1, 2, 3, 4, 5]

result = [item * 2 for item in my_list]
print(result)
# [2, 4, 6, 8, 10]
