
# Classes for project

class Ingredient:
    def __init__(self, ingredient):
        self.name = ingredient
        self.quantity = 0
        self.unit = ""
        self.restrictions = []
        # self.descriptor = ""
        # self.preparation = ""

    def set_quantity(self, q):
        self.quantity = q

    def set_unit(self, m):
        self.unit = m
    
    def set_restrictions(self, r):
        self.restrictions = r

    

    