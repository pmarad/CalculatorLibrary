
class Calculator:
    ''' Calculator function names and its functionality '''
    def __init__(self,*vals):
        self.vals = vals
    
    def add(self):
        return sum(self.vals)
    
calc = Calculator(1,2,3)
result = calc.add()
print(result)

