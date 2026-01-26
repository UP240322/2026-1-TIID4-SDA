import random
import time

def bubble_sort(arr):
    n = len(arr)
    arr_copy = arr.copy() # Crear una copia de arr para no modificar el original
    
    for i in range(n):
        # Flag para optimizar si ya está ordenado
        swapped = False
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes
            if arr_copy[j] > arr_copy[j + 1]:
                # Intercambiar si están en el orden incorrecto
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break
    
    return arr_copy

# Ejemplo de uso
if __name__ == "__main__":
    min = 11
    max = 20
    size = 10
    aleatorio = int(random.random() * ((max - min) + 1)) + min
    aleatorio = random.randint(min, max)

    lista = [64, 34, 25, 5, 22, 11, 90, 12]
    # generar una semilla aleatoria para reproducibilidad
    random.seed(42)

    lista = [random.randint(min, max) for _ in range(size)]

    print("\nLista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("\nLista ordenada:", lista_ordenada)

    # Medir tiempo de Bubble Sort
    start_time = time.perf_counter()
    sorted_bubble = bubble_sort(lista)
    end_time = time.perf_counter()
    bubble_time = (end_time - start_time) * 1000  # Convertir a milisegundos

    print(f"\n Bubble Sort:")
    print(f"   Tiempo de ejecución: {bubble_time:.4f} ms")
    