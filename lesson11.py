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
#         pass
#
#     def show_furniture(self):
#         print(f"show_furniture {self.name}, class arg - {self.high},{self.vidth}, obj_arg {self.high1}, {self.vidth1} ")
# # print(type(Furniture))
# # print(Furniture.__doc__)
# # print(Furniture.var_numb)
# # print(Furniture.show_furniture)
# table = Furniture(10, 20, 'table')  #create furniture object
# print(table.high)
# print(table.show_furniture())
#
# chair = Furniture(5, 7, 'Chair')
# print(chair.high)
# print(chair.show_furniture())
# print(chair.func())

class Furniture:
    """ Class Furniture """
    high = 1
    vidth = 2

    def __init__(self, high1, vidth1, name):
        self.high1 = high1
        self.vidth1 = vidth1
        self.name = name

    def func(self):
        print("Func in Furniture class")

    def show_furniture(self):
        print(f"show_furniture {self.name}, class arg - {self.high},{self.vidth}, obj_arg {self.high1}, {self.vidth1} ")


class Table(Furniture):
    table = 'table'

    # def func(self) -> str:
    #     return "Func in class Table"


table = Table(10, 20, 'table')
# print(table.show_furniture())
# print(table.func())

furn = Furniture(1, 2, 'furn')

# print(isinstance(table, Table))
# print(isinstance(table, Furniture))
# print(isinstance(furn, Furniture))
# print(isinstance(furn, Table))



