a = 0
if a <= 10:
    res = a+1
else:
    res = a+5
print(res)

a = 12
res = a+1 if a <= 10 else a+5
print(res)


# exceptions
#
# l = [1, 2, 3]
# a = 4
# #print(l[5])
# n = input('Please type numb:')
#
# try:
#     b = 2 + n
# except TypeError as e:
#     print("You type int instead of str")
# else:
#     print("something")
# finally:
#     print("the end")



# try:
#     print(l[1])
#     a/0
# # except Exception:
# #     print('list index out of range')
#
# except IndexError as e:
#     print(f'Error: {e}')
#
# except ZeroDivisionError as e:
#     print(f'Error: {e}')

m = {'a', 'b', 'c', 'a', 'b', 1, 4.7, (1,2,3,)}

# print(m)
#
# l = [1, 2,2,34,45, 4,4 ,345]
# print(l)
# l=set(l)
#
# print(l)
#
# l=[]
# s={}
# print(type(s))
# s1 = set()
# print(type(s1))

# for set_el in m:
#     print(set_el)
#
# print('f' in m)
#
# m.add('abc')
# print(m)
#
# l = [88, 99, 10]
# m.update(l)
# print(m)
#
# m.discard('abc')
# print(len(m))
#
# m1 = {'1',1, 7}
#
# print(m==m1)

# Compreehensions
# l = [1,2,3,4 ,5,6]
#
# l1=[]
# for i in l:
#     l1.append(i+1)
#
# print(l1)
#
# l2 = [i+1 for i in l if i > 2]
# print(l2)
#
# l3 = [x*2 for x in range(10)]
# print(l3)

# d = {x: x+1 for x in range(10)}
# print(d)
#
# g = (x+1 for x in range(10))
# print(type(g))
#
# for g_el in g:
#     print(g_el)

# Гра ДЗ

"""
За допомогою рандом генеруемо число (0-10)
виводимо це число на екран

Вводимо число з клавіатри 

Якщо числа співпадаюсь то гра закінчена

Якщо не співпадають то повторюемо заново 

всі дії доки не співпаде
"""