#
# def new_f(a=2, b=3):
#     # par = 1 #local
#     # par2 = 2 #local
#     print(f'a = {a}, b = {b}  ')
#     res = a+b
#     return res
#
# print(f' Result {new_f()}')
# print(f' Result {new_f(3,4)}')
# print(f' Result {new_f(4)}')





# def new_f(name, sername):
#     print(f'Hello Name-{name} Surmane-{sername} ')
#     return f'Hello {name} {sername}'
#
# print(new_f('John', 'Lenon'))



# def new_f(a, b, name=None, sername=None):
#
#     print(f'Hello positional {a, b} Name-{name} Surmane-{sername} ')
#     return f'Hello positional {a, b} Name-{name} Surmane-{sername} '
#
# print(new_f('a', 'b', sername='Lenon',name='John'))

# lst = [1, 2, 3]
#
# def new_f(a, b, var1, *args):
#     lst1 = []
#     lst1.append(a)
#     lst1.append(b)
#     lst1.append(var1)
#     print(type(args))
#     print(f'Args {args}')
#     for i in args:
#         print(f"Elem: {i}")
#         lst1.append(i+1)
#     return lst1
#
# print(new_f(5, 6, 7, 8, 9 , 10, 11))

# f_dict = {'a': 1, 'b': 2, 'name': 'John', 'surn': 'Lenon'}
#
# def new_f(a, name="Jonh", *args, **kwargs):
#     print(type(kwargs))
#     lst = []
#     print(f'kwargs {kwargs}')
#     for k, v in kwargs.items():
#         print(f'key: {k}')
#         print(f'value: {v}')
#         lst.append((k, v),)
#     return lst
#
# print(new_f(**f_dict))


# def star():
#     inp = int(input("Please type number"))
#     l = ""
#     ran = range(0, inp)
#     for el in ran:
#         l += "*"
#         print(l)
#
# star()

def draw_tree(cosmic):
    for i in range(1, cosmic+1):
        spaces = " " * (cosmic - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# if __name__ == "__main__":
#     try:
#         cosmic = int(input("Величина ялинки: "))
#         draw_tree(cosmic)
#     except ValueError:
#         print("Помилка: лише цілі числа.")

draw_tree(5)