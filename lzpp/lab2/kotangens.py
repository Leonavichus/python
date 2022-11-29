import math
from main import Corner

class Kotangens(Corner):
    # Функция Котангенс
    def ratio_of_angles(self):
        kotangens = math.cos(self.corner)/math.sin(self.corner)
        return f"Котангенс = {kotangens}"