import math
from main import Value
from abc import ABC, abstractmethod
 
class Koseksns(Value):
    # Функция Косеканс
    def ratio_of_angles(self):
        koseksns = 1/math.sin(self.corner)
        return f"\nКосеканс = {koseksns}"

    # Виртуальный метод
    @abstractmethod
    def virtualMethod(self):
        pass