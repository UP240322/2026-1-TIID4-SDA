
def seleccionSort(arr):
    # crear una copia de arr
    arr_copy = arr[:]
    # arr_copy = arr.copy()

    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # min_value = arr.pop(min_idx)
        # arr.insert(i, min_value)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 5, 22, 11, 90, 12]
    lista = [7,12,9,11,3]
    print("Lista original:", lista)
    seleccionSort(lista)
    print("Lista ordenada:", lista)


