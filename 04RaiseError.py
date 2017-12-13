import math
class InvalidRadiusError(Exception):

    def __init__(self,radius):
        super(InvalidRadiusError, self).__init__()
        self.radius = radius
    def __str__(self):
        return "非法半径"+str(self.radius)
#
def calcCircleArea(radius):

    # 如果半径小于0，导致逻辑无法正常继续下去，抛出一个异常
    if radius < 0:

        # 抛出一个异常
        raise InvalidRadiusError(radius)

    area = math.pi * radius ** 2
    print("圆的面积是%.2f" % (area))

radius = eval(input("请输入圆的半径："))

try:
    calcCircleArea(radius)
except InvalidRadiusError as re:
    print(re)
    pass
