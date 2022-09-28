class Value:
    # Конструктор
    def __init__(self, corner):
        self.corner = corner

    def __str__(self):
        return f"Значение = {self.corner}"

    # Метод подсчета
    def ratio_of_angles(self):
        pass

if __name__ == '__main__':
    # Импорт
    from sekans import Sekans
    from koseksns import Koseksns
    from kotangens import Kotangens

    # Ввод данных
    a  = float(input("Введите занчение: ") or 1)
    value  = Value(a)
    b = value.corner
    vehicles = [Sekans(b), Koseksns(b), Kotangens(b)]
    if (a != 0):
        # Создание экземпляров класса
        for o in vehicles:
            try:
                # Вывод данных
                print(o.ratio_of_angles())
            except NotImplementedError:
                print("Метод не реализован")
    else:
        print("Ноль нельзя!")
