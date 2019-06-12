
class Calculator:
    ''' Calculator function names and its functionality '''
    def __init__(self,*vals):
        self.vals = vals
    
    def add(self):
        return sum(self.vals)
    


def addition(*vals):
    return sum(vals)



