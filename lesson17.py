# Iterator

# my_list = [1, 2, 3]
#
# iterator = iter(my_list)
#
# print(type(iterator))
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# my_str = 'abc'
#
# iterator = iter(my_str)
#
# print(next(iterator))
# #print(next(iterator))
# #print(next(iterator))
#
# for elem in iterator:
#     print(f"Elem {elem}")


# from itertools import count
#
# iterator_wo_end = count(1)
#
# for el in range(500):
#     print(next(iterator_wo_end))

# *args, **kwargs
# def sum_digits(*args):
#     res = 0
#     print(f'Args: {args} Type {type(args)}')
#     for dig in args:
#         res += dig
#     return res
#
# print(sum_digits(3))
# print(sum_digits(3, 5))
# print(sum_digits(3, 5, 4, 6, 7, 80))

# def sum_digits(a, b, *args):
#     res = 0
#     print(f'Args: {args} Type {type(args)}')
#     res += a
#     res += b
#     for dig in args:
#         res += dig
#     return res
#
# print(sum_digits(3, 7))
# print(sum_digits(3, 5, 4, 6, 7, 80))

# def sum_digits(*args, **kwargs):
#     res = 0
#     print(f'Args: {args} Type {type(args)}')
#     print(f'Kwargs: {kwargs} Type {type(kwargs)}')
#     for dig in args:
#         res += dig
#
#     for val in kwargs.values():
#         res +=val
#
#     return res
#
# print(sum_digits(a=1, b=3))
# print(sum_digits(a=3, b=5, c=4, d=6, e=7, f=80))

# def sum_digits(a, b=10, *args, **kwargs):
#     res = 0
#     res += a
#     res += b
#     print(f'Args: {args} Type {type(args)}')
#     for dig in args:
#         res += dig
#
#     print(f'Kwargs: {kwargs} Type {type(kwargs)}')
#     for val in kwargs.values():
#         res +=val
#     return res
#
# print(sum_digits(a=1))
# print(sum_digits(a=1, b=2))
# print(sum_digits(5, 5, 6, 7, f=8, g=9, c=10))

# Decorator

# def decorated(func):
#     def wrapper():
#         print("Before func")
#         func()
#         print('After func')
#     return wrapper
#
#
# @decorated
# def hello():
#     print('Hello')
#
# print(hello())

def decorated(func):
    def wrapper(*args, **kwargs):
        print("Before func")
        res = func(*args, **kwargs)
        print(res)
        print('After func')
        return res
    return wrapper


@decorated
def hello(name):
    mes = f'Hello {name}'
    return mes

print(hello('John'))
print(hello('Bill'))
