
class Nodo:
    def __init__(self, data, siguiente=None):
        self.data = data
        self.siguiente = siguiente

    def __str__(self):
        return str(self.data)