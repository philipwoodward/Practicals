


class OldGuitars:
    def __init__(self, name='', year=0, cost=0.00):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{},  {},  {},  {}".format\
        (self.name,self.year,self.cost)