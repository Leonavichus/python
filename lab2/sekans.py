import math
from main import Value
 
class Sekans(Value):
    # Функция Секанс
    def ratio_of_angles(self):
        # Перегрузка метода
        super().ratio_of_angles()
        sekans = 1/math.cos(self.corner)
        return f"\nСеканс = {sekans}"