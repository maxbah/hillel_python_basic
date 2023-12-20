# var = 10
#
# print(f'global var before {var}')
# def func():
#     global var
#     #var=2
#     var += 1
#     print(f'var in func {var}')
#
# func()
# print(f'global var after {var}')
# var = 10
#
# print(f'global var before {var}')
# def func():
#     var = 10
#     var += 1
#     print(f'var in func {var}')
#     return var
# var = func()
#
# print(f'global var after {var}')

# n! = n*f(n-1)

# def factorial_rec(n):
#     if n in (0, 1):
#         return 1
#     return n*factorial_rec(n-1)
#
# print(factorial_rec(6))
#
# lst = [1, 2, 3, [4, 5, 6]]

# def rec(lst):
#     for i in lst:
#         print(i)
#         print(type(i))
#         if type(i) is list:
#             return rec(i)
#
# rec(lst)

#0 1 2 3 5 8
# f(n)=f(n-1)+f(n-2)

#
# def fibon_rec(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibon_rec(n - 1) + fibon_rec(n - 2)
#
#
# print(fibon_rec(9))

# def fibo(n):
#     fib1=fib2=1
#     if n in (1, 2):
#         return fib1
#     for i in range(n-2):
#         fib1, fib2 = fib2, fib1+fib2
#     return fib2
#
# print(fibo(9))

l = [1,2,3,6,7,8,5,9]

def calc_sum_numbers(l):
    if l == []:
        return 0
    else:
        sum = calc_sum_numbers(l[1:])
        sum = sum + l[0]
        return sum

l1 = [1, 2, 3]
print(calc_sum_numbers(l))

maybee its normal too)
def calc_sum_numbers(l):
    if not l:
        return 0
    else:
        rest_sum = calc_sum_numbers(l[1:])
        return l[0] + rest_sum

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(calc_sum_numbers(l1))


