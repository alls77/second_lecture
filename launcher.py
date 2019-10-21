import turtle

import Curve
from Draw import Draw


order = int(input('Enter the order number for the curve - '))

t= turtle.Turtle()
t.speed(150)
t.penup()
t.setposition(-50,-50)
t.pendown()

curve = Curve.GilbertCurve(order)
Draw.draw_curve(t, curve)

turtle.done()
