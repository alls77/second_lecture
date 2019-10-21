import LSystem
from Path import Path


class Curve:
    """Abstract curve"""

    def __init__(self, order):
        self.l_system = LSystem
        self.order = order

    def get_path(self):
        pass


class GilbertCurve(Curve):
    """"Gilbert Curve"""

    def __init__(self, order):
        Curve.__init__(self, order)

        self.l_system.alphabet = {'A', 'B'}
        self.l_system.constants = {'F', '+', '-'}
        self.l_system.axiom = 'A'
        self.l_system.rules = {
            'A': '-BF+AFA+FB-',
            'B': '+AF-BFB-FA+',
        }
        self.l_system.angle = 90

    def get_path(self):
        return Path.calculate_path(curve=self)
