import math
def getInput():
      d = float(input('enter the angle in degree :'))
      return d
def convDegree(degree):
    r = math.radians(degree)
    return r
def showValue(result):
    print("The angle in radians =",result)