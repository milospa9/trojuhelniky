triangle = turtle.Turtle()

def triangle_print(a, b, c):
    triangle.forward((c/2)*zooming)
    triangle.left(135)
    triangle.forward(a*zooming)
    triangle.left(90)
    triangle.forward(b*zooming)
    triangle.left(135)
    triangle.forward((c/2)*zooming)
    return None