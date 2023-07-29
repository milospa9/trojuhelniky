import math 
import turtle

rangeIndexStart = 1
rangeIndexEnd = 3
zooming=50

triangle = turtle.Turtle()
triangle.speed(1)
def triangle_print(a, b, c):
    triangle.forward((c/2)*zooming)
    triangle.left(135)
    triangle.forward(a*zooming)
    triangle.left(90)
    triangle.forward(b*zooming)
    triangle.left(135)
    triangle.forward((c/2)*zooming)
    return None

for i in range(rangeIndexStart,rangeIndexEnd):
    #rovnoramenny pravohuly trojuhelnik s N v c
    c=i
    a=math.sqrt((pow((c/2),2))+(pow((c/2),2)))
    b=math.sqrt((pow((c/2),2))+(pow((c/2),2)))
    triangle.color("red")
    triangle_print(a, b, c)

    #rovnoramenny pravohuly trojuhelnik s N v a a b
    x=i
    y=i
    z=math.sqrt((pow(x,2))+(pow(y,2)))
    triangle.color("blue")
    triangle_print(x, y, z)





turtle.done()


