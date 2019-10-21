class Draw:

    @staticmethod
    def draw_curve(turtle, curve):
        """"Draw curve"""

        commands = curve.get_path()
        step = 10

        for command in commands:
            if command == 'F':
                turtle.forward(step)
            elif command == '+':
                turtle.right(curve.l_system.angle)
            elif command == '-':
                turtle.left(curve.l_system.angle)
