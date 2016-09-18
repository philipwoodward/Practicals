


class ProgrammingLanguage:
    def __init__(self, name='', typing='Y', reflection=True, year=1991):
        """Initialise a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{},  {}, Reflection = {}, First appeared in {}".format\
        (self.name,self.typing,self.reflection,self.year)
