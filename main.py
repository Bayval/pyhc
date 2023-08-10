# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("Вызов new для " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0,y=0):
#         print("Вызов new для " + str(self))
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt)
import csv
d = {1:'-',}
with open("dataset_3380_5.txt") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        list_key=list(dict(row).keys())
        print(list_key)
