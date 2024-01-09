# class Line:
#     start = None
#     _start = 2  # protected
#     __start = 10  # private
#     end = None
#
#     def __init__(self, point1, point2): #agregation
#         self.start = point1
#         self.end = point2
#
#     @property
#     def length(self):
#         diffx = self.start.x - self.end.x
#         diffy = self.start.y - self.end.y
#         res = (diffx ** 2 + diffy**2) ** 0.5
#         return res
#
# l2 = Line(p1, p2)
# # print(f' Class method {l2.length()}')
#
# print(f'Atribut {l2.length}')
# print(f'Protected {l2._start}')
# print(f'Private {l2._Line__start}')
#
#
# class MyClass:
#     my_attr = 0
#
#     def __init__(self, val):
#         self.my_attr = val
#
#         def foo(self):
#             pass
#         self.foo = foo
#
#     # def foo(self):
#     #     pass
#
#     def __getattribute__(self, item):
#         print('In __getattribute__')
#         res = super().__getattribute__(item)
#         print(f'In __getattribute__ res {res}')
#         return res
#
#     def __getattr__(self, item):
#         print('In __getattr__')
#         return None
#
#     def __setattr__(self, key, value):
#         print("In __setattr__")
#         self.__dict__[key] = value
#
#
# obj = MyClass(10)
#
# print(obj.my_attr)
# getattr(obj, 'my_attr')
# print(obj.__dict__)
# print(obj.__class__.__dict__)
# obj.my_attr = 20
# print(obj.my_attr)
#
# class Myclass:
#     my_attr = 2
#
#
#
# obj = Myclass()
# obj2 = Myclass()
#
# # print(obj.my_attr)
# # print(obj2.my_attr)
#
# obj.my_attr = 10
#
# # print(obj.my_attr)
# # print(obj2.my_attr)
#
# Myclass.my_attr = 20
#
# print(obj.my_attr)
# print(obj2.my_attr)
import abc
# class Myclass:
#     my_attr = 2
#
#     def __getitem__(self, item):
#         print('In __getitem__')
#         return self.__dict__.get(item, self.__class__.__dict__.get(item))
#
#     def __setitem__(self, key, value):
#         print('In __setitem__')
#         self.__dict__[key] = value
#
#
#
# obj = Myclass()
#
# # Myclass.my_attr #class atributy
# # obj.my_attr #obj atribut
#
# print(obj['my_attr'])
# obj.my_attr = 100
#
# print(obj['my_attr'])

# class OnlyNumbers:
    # _name = ''
    #
    # def __init__(self, name):
    #     self._name = name

    # def __get__(self, instance, owner):
    #     print("in __get__")
    #     return getattr(instance, self._name)

    # def __set__(self, instance, value):
    #     print("in __set__")
    #     print(instance, value)
    #     if not instance(value, int):
    #         raise TypeError
    #     return setattr(instance, self._name, value)



# class MyClass:
#     my_attr = OnlyNumbers()
#
# obj = MyClass()
# print(obj.my_attr)
#obj.my_attr = 10
#obj.my_attr = 5.6
#obj.my_attr = 'jkhkj'

from abc import ABC


class Transport1(ABC):

    @abc.abstractmethod
    def move(self):
        pass


class Transport:
    def move(self):
        return self._move()

    def _move(self):
        raise NotImplemented


class Car(Transport):
    def _move(self):
        print("I'm car and I move")


class Bike(Transport):
    def _move(self):
        print("I'm bike and I move")

class Ship(Transport1):

    def move(self):
        print("I'm Ship and I can sweem")

car = Car()
bike = Bike()
ship = Ship()

ship.move()
# car.move()
# bike.move()

