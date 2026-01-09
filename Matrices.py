# Matriz de 4X3

Matriz = [[1, 2, 3],  
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

F = len(Matriz)        # Número de filas
C = len(Matriz[0])     # Número de columnas

for i in range(F):         # filas
    for j in range(C):     # columnas
        print(Matriz[i][j], end="\t")
    print()  # Nueva línea después de cada fila

# Salida: B
# obtener la transpuesta de la matriz sin usar reflecciones

#Transpuesta = [[0 for _ in range(F)] for _ in range(C)]
#for i in range(F):
#    for j in range(C):
#        Transpuesta[j][i] = Matriz[i][j]

Transpuesta = []
for j in range(C):
    nueva_fila = []
    for i in range(F):
        nueva_fila.append(Matriz[i][j])
    Transpuesta.append(nueva_fila)
    
print("Matriz Transpuesta:")
