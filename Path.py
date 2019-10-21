class Path:

    @staticmethod
    def calculate_path(curve):
        """"Calculate path"""

        path = curve.l_system.axiom

        for iteration in range(curve.order):
            new_path = ''

            for value in path:
                if value in curve.l_system.alphabet:
                    new_path += curve.l_system.rules[value]
                else:
                    new_path += value

            path = new_path

        return path
