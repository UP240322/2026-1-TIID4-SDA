# Entrada de datos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

F = len(matriz)        # número de filas
C = len(matriz[0])     # número de columnas

# Proceso: calcular la transpuesta
#transpuesta = [[0] * F for _ in range(C)]
transpuesta = [[0 for _ in range(F)] for _ in range(C)]

for i in range(F):
    for j in range(C):
        transpuesta[j][i] = matriz[i][j]

# Salida de datos
print("Matriz Original:")
for i in range(F):
    for j in range(C):
        print(matriz[i][j], end="\t")
    print()

print("\nMatriz Transpuesta:")
for i in range(C):
    for j in range(F):
        print(transpuesta[i][j], end="\t")
    print()
