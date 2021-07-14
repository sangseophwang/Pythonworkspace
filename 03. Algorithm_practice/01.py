# list comprehension
_list = []
for num in range(1, 11):
    _list.append(num)


# [expression for component in input_sequence <if statement>]

_list = [num for num in range(1, 11)]


# 2, 4, 6, 8 등등

_list = [num * 2 for num in range(1, 11)]


# 주어진 리스트를 받아서 3의 배수만 저장하자.
ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_list = []
for num in ref:
    if num % 3 == 0:
        _list.append(num)

_list = [num for num in ref if num % 3 == 0]


# 변수 거꾸로 담기

aa = [(2, 3), (1, 4), (5, 6), (6, 1), (2, 3)]

_list = [(b, a) for a, b in aa]


# 주어진 리스트를 그대로 담되, 15가 넘는 숫자는 15로 저장하는 리스트를 만들어보자.

ref = [2, 4, 16, 13, 16, 12, 66, 23, 40]

_list = [num if num <= 15 else 15 for num in ref]
