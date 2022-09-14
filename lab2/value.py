class Value:
    def __init__(self, corner):
        self.corner = corner

if __name__ == '__main__':
    from sekans import Sekans
    from koseksns import Koseksns
    from kotangens import Kotangens

    a  = float(input("Введите занчение: "))
    sekans = Sekans(a)
    koseksns = Koseksns(a)
    kotangens = Kotangens(a)
    print(sekans.ratio_of_angles(),koseksns.ratio_of_angles(), kotangens.ratio_of_angles())
