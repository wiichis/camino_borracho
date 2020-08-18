import random


class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class Lucheins(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([
            (0, random.random()),
            (0, random.random() * -1),
            (random.random(), 0),
            (random.random() * -1, 0),
        ])