from Nodo import *


class Laboratorio:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # Verificar si la lista está vacía
    def empty(self):
        return self.first is None

    # Insertar un elemento en la lista
    def insert(self, data):
        new_nodo = Nodo(data)

        if self.empty():
            self.first = new_nodo
            self.last = new_nodo
        else:
            self.last.siguiente = new_nodo
            self.last = new_nodo
        self.size += 1

    # Opcionalmente, puedes definir un método __str__ para imprimir la lista
    def __str__(self):
        result = []
        current = self.first
        while current:
            result.append(str(current))
            current = current.siguiente
        return " -> ".join(result)
