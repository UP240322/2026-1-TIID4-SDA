# expresion comprehension para crear una matriz 5x3 FxC
# Se lee de Derecha a Izquierda
A = [[0 for _ in range(3)] for _ in range(5)]
print(A)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# A =[
#    [0, 0, 0], 
#    [0, 0, 0], 
#    [0, 0, 0], 
#    [0, 0, 0],
#    [0, 0, 0]
#   ]

# Asignacion de valores a la matriz
A[0][0] = 1
print(A)

# Forma equivalente usando bucles anidados
print("\nForma equivalente usando bucles anidados")
B = []
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(0)
    B.append(fila)
print(B)
B.append([0, 0, 0])
print(B)

