import re

# my_str = "abcd aa 111 %#$"
#
# tmp = 'rabc'
#
# res = re.match(tmp, my_str)
# print(res)

# my_str = "abcd aa 111aa %#$"
#
# tmp = 'aa'
#
# res = re.search(tmp, my_str)
# print(res)

# my_str = "aabcd aa 111aa %#$"
#
# tmp = 'aa'
#
# res = re.findall(tmp, my_str)
# print(res)

# my_str = "aabcd aa 111aa %#$"
#
# tmp = 'aa'
#
# res = re.finditer(tmp, my_str)
# for i in res:
#     print(i)

# my_str = "4aabcdaa 111aa %#$"
#
# tmp = '[0-9][a-z]{6}'
#
# # Meta . ^ $ () {} [] / | ? * +
# # [0123456789] -> [0-9]
# # [abcdefghklmnopqrstuvwxyz] -> [a-zA-Z0-9]
# res = re.search(tmp, my_str)
#
# print(res)

# my_str = 'petr.petrov-1@gmail.mail.com'
#
# tml = '[a-zA-Z0-9_-]{1,10}\.{0,1}[a-zA-Z0-9-]{1,10}@[a-zA-Z0-9.-]{1,10}\.{0,1}[a-zA-Z0-9.-]{1,10}'
#
# res = re.search(tml, my_str)
# print(res)
# res1 = [i for i in range(1000000000)]
# for i in res1:
#     print(i)
# res = (i for i in range(10000000))
# for i in res:
#     print(next(res))
#
# print(next(res))
# print(res)
# Thread

import threading
import time

# def foo(name, delay):
#     print(f'Hello {name}\n')
#     time.sleep(delay)
#
# th1 = threading.Thread(target=foo, args=('thread1', 0.2))
# th2 = threading.Thread(target=foo, args=('thread2', 0.5))
#
# th1.start()
# th2.start()

counter = 0
threads = []

def foo():
    global counter
    for i in range(100000):
        value = counter
        value += 1
        lst = [j for j in range(100)]
        counter = value

for i in range(5):
    thread = threading.Thread(target=foo)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()
print(f'Counter - {counter}')



