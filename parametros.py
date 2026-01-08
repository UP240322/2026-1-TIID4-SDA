# main.py
import sys

if __name__ == "__main__":
    for i, dato in enumerate(sys.argv):
        print(f"Argumento {i}: {dato}")

    for dato in sys.argv:
        print(f"Argumento: {dato}")



    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        print(f"Hola, {nombre}!")
    else:
        print("Hola, mundo!")

    # for que cuenta de 0 a 4
    # for i in range(5):
    #     print(f"Contador: {i}")
