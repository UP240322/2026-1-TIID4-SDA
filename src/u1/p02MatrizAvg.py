# Entrada de datos
alumnos = ["Ana", "Carlos", "Marta", "Hugo", "Luis"]
materias = ["Matemáticas", "Física", "Química", "Biología"]
calificaciones = [
    [10, 9, 8, 7],
    [9, 7, 6, 8],
    [8, 9, 5, 9],
    [7, 8, 9, 10],
    [6, 7, 8, 9]
]

# Proceso: obtener el promedio de alumnos y materias
F = len(calificaciones)        # número de filas (alumnos)
C = len(calificaciones[0])     # número de columnas (materias)

avg_alumnos = [0.0] * F
avg_materias = [0.0 for _ in range(C)]   # lista por comprensión
avg_total = 0.0

for i in range(F):
    for j in range(C):
        avg_alumnos[i] += calificaciones[i][j] / C
        avg_materias[j] += calificaciones[i][j] / F
        avg_total += calificaciones[i][j] / (F * C)

# Salida de datos
print(f"{'Alumnos/Materias':<20}", end="")
for materia in materias:
    print(f"{materia:<15}", end="")
print(f"{'Promedio':<15}")

for i in range(F):
    print(f"{alumnos[i]:<20}", end="")
    for j in range(C):
        print(f"{calificaciones[i][j]:<15.2f}", end="")
    print(f"{avg_alumnos[i]:<15.2f}")

print(f"{'Promedio':<20}", end="")
for promedio in avg_materias:
    print(f"{promedio:<15.2f}", end="")
print(f"{avg_total:<15.2f}")
