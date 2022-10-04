import math
from main import Corner
from abc import ABC, abstractmethod
 
class Koseksns(Corner):
    # Функция Косеканс
    def ratio_of_angles(self):
        koseksns = 1/math.sin(self.corner)
        return f"Косеканс = {koseksns}"

    # Виртуальный метод
    @abstractmethod
    def virtualMethod(self):
        pass