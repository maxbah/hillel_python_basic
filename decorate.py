import datetime
from libr.fact import factorial_rec


def calc(a, b, c):
    return a*b**c


def time_decor(func): # створюємо функцію декоратор котра приймає один агрумент функцію над якою буде виконуватись декорування
    def wrapper(*args, **kwargs): # строрюємо функцію обгортку- тут буде все те що ми будемо додавати до функції яку декоруєсо
        start = datetime.datetime.now()
        print(f'start {start}')
        res = func(*args, **kwargs) # виконуємо нашу функцію
        end = datetime.datetime.now()
        print(f'end {end}')
        delta = end - start
        print(f"Runtime: {delta}")
        return res # повертаємо результат функції яку передаємо декоратору як агрумент
    return wrapper # повертаємо враппер без його виклику на виконання


@time_decor # додаемо декорато
def fact_decorated(n): # створюємо функцію яку будемо декорувати
    return factorial_rec(n) # повертаємо нашу функію факторіал

# print(factorial_rec(5))
print(fact_decorated(50)) # виконуемо декоровану функцію

@time_decor
def calc_decor(a, b, c):
    return calc(a, b, c)

print(calc(3, 4, 5))
print(calc_decor(3, 4, 5))
