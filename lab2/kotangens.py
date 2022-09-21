import math
from main import Value

class Kotangens(Value):
    # Функция Котангенс
    def ratio_of_angles(self):
        kotangens = math.cos(self.corner)/math.sin(self.corner)
        return f"\nКотангенс = {kotangens}"