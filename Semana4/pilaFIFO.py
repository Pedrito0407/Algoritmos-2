pilaNombres = []

# Ingreso de nombres
for i in range(20):
    n = input(f"Ingrese el nombre #{i+1}: ")
    pilaNombres.append(n)

print("\nPila inicial:", pilaNombres)

# Eliminar el último nombre ingresado
eliminado = pilaNombres.pop(0)
print(f"\n¡Nombre eliminado (último ingresado): '{eliminado}'!")

print("\nPila actualizada:", pilaNombres)


