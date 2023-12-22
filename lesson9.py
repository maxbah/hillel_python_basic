# def outer(a, b):
#     print(a, b)
#     def inner_in(x, y):
#         print(x, y)
#         return a+b+x+y
#     return inner_in
#
#
# out = outer(1, 2)
# res = out(3, 4)
#
# print(res)

# def add(x, y):
#     return x+y
#
# def calculate(func, x, y):
#     return func(x, y)
#
# res = calculate(add, 1, 2)
# print(res)

# def decorator(func):
#     def wrapper():
#         print("I decorated")
#         func()
#         print('after function')
#     return wrapper
#
#
# def foo():
#     print("I'm ordinary function")
#
# print(foo())
#
# # decorator
# dec = decorator(foo)
# print(dec())
#
# def decorator(func):
#     def wrapper():
#         print("I decorated")
#         func()
#         print('after function')
#     return wrapper
#
# def decorator1(func):
#     def wrapper():
#         print("I second decorated")
#         func()
#         print('after second function')
#     return wrapper
#
#
# @decorator
# def foo():
#     print("I'm ordinary function")
#
# print(foo())

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("I decorated")
#         res = func(*args, **kwargs)
#         print('after function')
#         return res
#     return wrapper
#
#
# @decorator
# def foo(*args, **kwargs):
#     print(f"args {args}, kwargs {kwargs}")
#
# print(foo(1, 4, name="Jonh", sur="Lenon"))
#---------------------------------------------------



