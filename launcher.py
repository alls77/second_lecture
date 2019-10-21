import turtle

import Curve
from Draw import Draw


order = int(input('Enter the order number for the curve - '))

turtle.speed(150)
turtle.penup()
turtle.setposition(0,0)
turtle.pendown()

curve = Curve.GilbertCurve(order)
Draw.draw_curve(curve)
