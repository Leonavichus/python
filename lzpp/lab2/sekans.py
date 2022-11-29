import math
from main import Corner
 
class Sekans(Corner):
    def ratio_of_angles(self):
        # Перегрузка метода
        super().ratio_of_angles()
        sekans = 1/math.cos(self.corner)
        return f"Секанс = {sekans}"