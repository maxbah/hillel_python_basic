import libr.our_func


# def print_fun():
#     libr.our_func.f1()
#     libr.our_func.f2()
#     libr.our_func.f3()


# if __name__ == '__main__':
#     print_fun()
#     print(f' __name__ : {__name__}')


# def print_func(a, b):
#     """ Function for adding a+b
#     """
#     res = {a + b}
#     print(f'res = {res}')
#     return res

# def print_func(a, b):
#     """
#     Function for adding a+b
#
#     :param a: str/int
#     :param b: str/int
#     :return: str/int
#     """
#     res = {a + b}
#     print(f'res = {res}')
#     return res

# var: int = 3
#
#
# def print_func(a: int, b: int) -> float:
#     """
#     Function for adding a+b
#
#     :param a: str/int
#     :param b: str/int
#     :return: str/int
#     """
#     res = a + b
#     print(f'res = {res}')
#     return float(res)
#
# print(print_func(1, 3), type(print_func(1, 3)))
# print(print_func.__doc__)

#useful functions

# a = int('123')
#
# print(a, type(a))
#
#
# def func(v):
#     return v % 2
#
# res = min([1, 3, 4,-2], key=func)
# print(f'res = {res}')
#
# res1 = max([2, 3, 4,-2], key=func)
#
# print(f'Max: {res1}')

# lambda x: x % 2
# # 2
#
# res = min([1, 3, 4, -2], key=lambda x: x % 2)
# print(f'res = {res}')

#print(lambda x: x % 2)

# lst = [1, 2, 3, 4, 5, 6]
#
# def func(lst):
#     if lst % 2 == 0:
#         return True
#     return False
#
# sep_slt = filter(func, lst)
#
# print(lst)
# print(list(sep_slt))

# lst = [1, 2, 3, 4]
# lst1 = ['a', 'b', 'c', 'd']

# (1, 'a'), (2:'b'),

# def func(lst):
#     res = lst+1
#     return res
#
# map_f = map(func, lst)
# print(list(map_f))

# print(func(lst))
#
# lst = [1, 2, 3, 4, 5, 7]
# lst1 = ['a', 'b', 'c']
# lst2 = [6, 7, 8, 9]
#
# # (1, 'a'), (2:'b')
# ziped = zip(lst, lst1, lst2)
#
# print(list(ziped))
# for i in ziped:
#     print(i)


"""Напишіть функцію яка отримує 3 аругменти: 
перші 2 числа і третій аргумент 
- операція яку треба виконати над цими 2-а числами
операції +, -, *, /
У випадку невіддомої операції вивести повідомлення - 
Невідома операція"""