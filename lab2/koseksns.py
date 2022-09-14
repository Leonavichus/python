import math
from value import Value
 
class Koseksns(Value):
    def ratio_of_angles(self):
        koseksns = 1/math.sin(self.corner)
        return f"\nКосеканс = {koseksns}"