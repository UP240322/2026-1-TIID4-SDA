nombres = ['Ana', 'Luis', 'Carlos', 'Marta']
materias = ['','Matemáticas', 'Física', 'Química', 'Biología']
calificaciones = [[10, 9, 8, 7],
                  [9, 7, 6, 8],
                  [8, 9, 5, 9],
                  [7, 8, 9, 10]]

F = len(calificaciones)        # Número de filas
C = len(calificaciones[0])     # Número de columnas
# print("\t" , end="")
for i in range(C+1):         # filas
    print(materias[i], end="\t")
print()

for i in range(F):         # filas
    for j in range(C):     # columnas
        print(calificaciones[i][j], end="\t")
    print()  # Nueva línea después de cada fila
