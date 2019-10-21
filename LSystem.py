from dataclasses import dataclass


@dataclass
class LSystem:
    """"L-system model"""

    alphabet: set
    constants: set
    axiom: str
    rules: dict
    angle: int
