pilaFia = []
pilaFia2 = []

# Push inicial
for i in range(15):
    pilaFia.append(i+1)

print("Pila inicial:", pilaFia)

sacarNumero = [3, 7]

# Sacar elementos hasta vaciar la pila
while pilaFia:
    temp = pilaFia.pop()
    if temp in sacarNumero:
        print(f"¡Número {temp} eliminado!")
        # No lo agregamos a pilaFia2
    else:
        pilaFia2.append(temp)


# Restaurar la pila original sin los números eliminados
while pilaFia2:
    pilaFia.append(pilaFia2.pop())

print("Pila restaurada (sin los números eliminados):", pilaFia)
