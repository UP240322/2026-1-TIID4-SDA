import random
import time

def insertion_sort(arr): # mejorado
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(1,n):
        insert_index = i
        current_value = arr_copy[i]
        for j in range(i-1, -1, -1):
            if arr_copy[j] > current_value:
                arr_copy[j+1] = arr_copy[j]
                insert_index = j
            else:
                break
        arr_copy[insert_index] = current_value
    return arr_copy

if __name__ == "__main__":
    min = 11
    max = 20
    size = 10_000
    random.seed(42)

    lista = [random.randint(min, max) for _ in range(size)]
    lista = [7, 12, 9, 11, 3]
    start_time = time.perf_counter()
    print(start_time)
    sorted_insertion = insertion_sort(lista)
    end_time = time.perf_counter()
    print(end_time)
    insertion_time = (end_time - start_time) * 1000  # Convertir a milisegundos

    print(f"\n Insertion Sort:")
    print(f"   Tiempo de ejecución: {insertion_time:.4f} ms")

    sample_array = [5, 2, 9, 1, 5, 6]
    sorted_array = insertion_sort(sample_array)
    print("Original array:", sample_array)
    print("Sorted array:", sorted_array)
    

