#
# print('hello Jonh')
# print('hello Jonh')
# print('hello Jonh')
# print('hello Jonh')


# def print_hello():
#     c = 'Hello Jonh'
#     for i in range(10):
#         if i > 5:
#             print(f"i = {i}")


# def summa_a_plus_b():
#     summa = 2 + 4
#     print(f"Summa = {summa}")
#     return summa
#
# b = summa_a_plus_b()
# print('B:', b)
# print(summa_a_plus_b())
g = 10  # global

# def summa_a_plus_b():
#     a = 2 #local
#     b = 4 #local
#     summa = a + b + g
#     print(f"Summa = {summa}")
#     return summa
#
# print(g)
# print(summa_a_plus_b())


# def summa_a_plus_b(a, b, c=5):
#     summa = a + b + c
#     print(f"Summa = {summa}")
#     return summa
#
# print(g)
# print(summa_a_plus_b(4, 2))
#print(summa_a_plus_b("abc", "d"))
#print(summa_a_plus_b(6, 14))


# def summa_a_plus_b(a, b, first=None, second=10):
#     summa = a+b+first + second
#     print(f"Summa = {summa}")
#     return summa
#
# print(g)
# print(summa_a_plus_b(2, 3, first=4, second=2))

# def add_to_list(a, lst=[]):
#     lst.append(a)
#     print(f"Lst = {lst}")
#     return lst
#
# print(add_to_list(1, lst=[]))
# print(add_to_list(1))
# print(add_to_list(1))
# print(add_to_list(1))


# def add_to_list(a, num=4, *args):
#     print(type(args))
#     print(args)
#     lst = []
#     lst.append(a)
#     lst.append(num)
#     for i in args:
#         lst.append(i)
#     print(f"Lst: {lst}")
#     return lst
#
# print(add_to_list(1, 2, 3, 4, 'b', 'd', True, ('a', 'b', 'c')))

lst = [1, 2, 3, 4, 5]

def add_to_list(*par):
    print(type(par))
    print(par)
    lst = []
    for i in par:
        lst.append(i+1)
    print(f"Lst: {lst}")
    return lst

print(add_to_list(*lst))




