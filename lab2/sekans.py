import math
from value import Value
 
class Sekans(Value):
    def ratio_of_angles(self):
        sekans = 1/math.cos(self.corner)
        return f"Секанс = {sekans}"