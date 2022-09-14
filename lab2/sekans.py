import math
from main import Value
 
class Sekans(Value):
    def ratio_of_angles(self):
        super().ratio_of_angles()
        sekans = 1/math.cos(self.corner)
        return f"\nСеканс = {sekans}"