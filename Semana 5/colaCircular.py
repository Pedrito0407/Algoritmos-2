class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.queue = [None] * capacidad
        self.frente = -1
        self.final = -1
        self.tamaño = 0

    def enqueue(self, elemento):
        if self.isFull():
            return "La cola está llena"
        
        if self.isEmpty():
            self.frente = 0

        self.final = (self.final + 1) % self.capacidad
        self.queue[self.final] = elemento
        self.tamaño += 1

    def dequeue(self):
        if self.isEmpty():
            return "La cola está vacía"

        elemento = self.queue[self.frente]
        self.queue[self.frente] = None  # Limpia el valor (opcional)
        self.frente = (self.frente + 1) % self.capacidad
        self.tamaño -= 1

        if self.tamaño == 0:  # Resetea punteros si queda vacía
            self.frente = -1
            self.final = -1

        return elemento

    def peek(self):
        if self.isEmpty():
            return "La cola está vacía"
        return self.queue[self.frente]

    def isEmpty(self):
        return self.tamaño == 0

    def isFull(self):
        return self.tamaño == self.capacidad

    def size(self):
        return self.tamaño

    def mostrarCola(self):
        if self.isEmpty():
            return []
        resultado = []
        i = self.frente
        for _ in range(self.tamaño):
            resultado.append(self.queue[i])
            i = (i + 1) % self.capacidad
        return resultado


# Crear una cola circular con capacidad de 5
cola = ColaCircular(5)

cola.enqueue('Aldo')
cola.enqueue('Bianca')
cola.enqueue('Carlos')

print("Cola: ", cola.mostrarCola())
print("Primer elemento: ", cola.peek())
print("Elimina: ", cola.dequeue())
print("Cola después de eliminar: ", cola.mostrarCola())
print("Está vacía: ", cola.isEmpty())
print("Tamaño: ", cola.size())

cola.enqueue('Diana')
cola.enqueue('Elena')
cola.enqueue('Fernando')  # Llena la cola

print("Cola después de agregar más elementos: ", cola.mostrarCola())
print("Intentar agregar más: ", cola.enqueue('Gustavo'))  # Debe indicar que está llena
print("Nuevo primer elemento: ", cola.peek())
print("Tamaño: ", cola.size())
