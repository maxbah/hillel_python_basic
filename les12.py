# class Furniture:
#     """ Class Furniture """
#     high = 1
#     vidth = 2
#
#     def __init__(self, high1, vidth1, name):
#         self.high1 = high1
#         self.vidth1 = vidth1
#         self.name = name
#
#     def func(self):
#         print("Func in Furniture class")
#
#     def show_furniture(self):
#         print(f"show_furniture {self.name}, class arg - {self.high},{self.vidth}, obj_arg {self.high1}, {self.vidth1} ")
#
#
# class Table(Furniture):
#     table = 'table'
#     color = ''
#
#     def __init__(self, high1, vidth1, name, color):
#         super().__init__(high1, vidth1, name)
#         self.color = color
#
#     # def func(self) -> str:
#     #     return "Func in class Table"
#
#
# table = Table(10, 20, 'table', 'red')
# print(table.high)
# print(table.color)
# print(table.name)
# # print(table.show_furniture())
# # print(table.func())
#
# furn = Furniture(5, 2, 'furn')
# furn2 = Furniture(7, 2, 'furn2')
#
# print(Furniture.high) # class atr
# print(furn.high1) # object atr
# print(furn2.high1) # object atr
#

class Point:
    x=0
    y=0

    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise TypeError

    def __str__(self):
        return f'Point {self.x} : {self.y}'

    def __add__(self, other):
        line = Line(self, other)
        return line

p1=Point(1,1)
p2=Point(5,5)
# print(p1)
# print(p2)
# p3 = Point('sadlkfj', [])
# print(p3)


class Line:
    start = None
    end = None

    # def __new__(cls, *args, **kwargs):
    #     isinstance=object.__new__(cls)
    #     return isinstance

    def __init__(self, point1, point2): #agregation
        self.start = point1
        self.end = point2

    def length(self):
        diffx = self.start.x - self.end.x
        diffy = self.start.y - self.end.y
        res = (diffx ** 2 + diffy**2) ** 0.5
        return res

    def __gt__(self, other):
        print('In greater')
        return self.length() > other.length()

    def __lt__(self, other):
        print('In lower')
        return self.length() < other.length()

    def __ge__(self, other):
        print('In greater equal')
        return self.length() >= other.length()

    def __le__(self, other):
        print('In less equal')
        return self.length() <= other.length()

    def __eq__(self, other):
        print('In equal')
        return self.length() == other.length()

    def __ne__(self, other):
        print('In not equal')
        return self.length() != other.length()

    # def __add__(self, other):
    #     line = Line(self.other)
    #     return line

    # def __init__(self, x, y, x1, y1): #composition
    #     self.start = Point(x, y)
    #     self.end = Point(x1, y1)

    def __str__(self):
        return f'Line start {self.start} end {self.end}'
    

p3 = Point(0,0)
p4 = Point(0,6)

l = Line(p1, p2)
l2 = Line(p3, p4)


# print(l.length() > l2.length())
# print(l <= l2)
# print(l == l2)
#
# print(l2.length())
# l1 = Line(2, 2, 8, 8)
# print(l1)

line = p3 + p4
print(line)





""""""