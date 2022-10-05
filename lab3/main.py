class Country:
    def __init__(self, idC, name):
        self.idC = idC
        self.name = name
        self.next = None

class City:
    def __init__(self, idC, name):
        self.idS = idS
        self.name = name

class Street:
    def __init__(self, idSt, name):
        self.idSt = idSt
        self.name = name
        self.next = None