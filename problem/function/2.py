# page 10

def dist(x1, y1, x2, y2):
    return((float(x1) - float(x2))**2 + (float(y1) - float(y2))**2)**0.5


point1 = input("Enter first point (x y) : ")
point2 = input("Enter second point (x y) : ")

x1, y1 = point1.split()
x2, y2 = point2.split()
distance = dist(x1, y1, x2, y2)
print('Distance of', point1, 'and', point2, 'is', distance)
