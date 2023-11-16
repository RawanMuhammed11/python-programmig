import math
def recpol(x, y):
    if x >= 0 and y >= 0:
        r = math.sqrt(x**2 + y**2)
        theta = math.atan(y / x)
#to make the conversions from rectangular to polar coordinates in the range from 0 to 2pi
    if x < 0:
        theta =theta+ math.pi  # Add 180 degrees for the second and third quadrants
    elif y < 0:
        theta = theta + (2 * math.pi)  # Add 360 degrees for the fourth quadrant

    return r, theta

x = int(input("Enter x: "))
y = int(input("Enter y: "))

polar_coordinates = recpol(x, y)
print(f"Rectangular coordinates ({x}, {y}) in polar coordinates are: {polar_coordinates}")