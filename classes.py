
# Classes for project

class Ingredient:
    def __init__(self, ingredient):
        self.name = ingredient
        self.quantity = 0
        self.measurement = ""
        # self.descriptor = ""
        # self.preparation = ""

    def set_quantity(self, q):
        self.quantity = q

    def set_measurement(self, m):
        self.measurement = m