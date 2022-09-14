class Value:
    def __init__(self, corner):
        self.corner = corner

    def __str__(self):
        return f"Значение = {self.corner}"

    def ratio_of_angles(self):
        pass

if __name__ == '__main__':
    from sekans import Sekans
    from koseksns import Koseksns
    from kotangens import Kotangens

    a  = float(input("Введите занчение: ") or 1)
    value  = Value(a)
    if (a != 0):
        sekans = Sekans(value.corner)
        koseksns = Koseksns(value.corner)
        kotangens = Kotangens(value.corner)
        print(value, sekans.ratio_of_angles(),koseksns.ratio_of_angles(), kotangens.ratio_of_angles())
    else:
        print("Ноль нельзя!")
