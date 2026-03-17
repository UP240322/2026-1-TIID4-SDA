# PS G:\Mi unidad\home\core\code\2026-1-TIID4-SDA> python.exe -m src.u3.testTree 
import os, sys

# from src.u3.Tree_BST import minValueNode
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Agrega el directorio raíz al path. Usar cuando no hay __init__.py

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Necesario para Fn.py

from Tree import Tree
from mat.Fn import Fn, sumar

def main():
    #fn = Fn()
    #fn.suma(5, 10)  # Llamada a la función suma de la clase Fn
    #sumar(5, 10)  # Llamada a la función sumar de la clase Fn
    myH = Tree()
    myH.show(myH.root)

    myH.insert("Melchor")
    myH.insert("Gaspar")
    myH.insert("Obama")
    myH.insert("Nava")
    myH.insert("Perez")

    print("\nÁrbol en forma gráfica:")
    myH.show(myH.root)

    print("\nRecorrido inorder:")
    myH.inorder()          # Llamada sin parametro
    # myH.inorder(myH.root)  # Llamada con parametro

    print("\n\nBuscar 'Gaspar':", myH.search(myH.root, "Gaspar"))
    print("Buscar 'Carlos':", myH.search(myH.root, "Carlos"))

    #print("\nLowest value:",minValueNode(myH.root).data)
    print("\nLowest value:",myH.minValueNode(myH.root).data)
    
    myH.delete("Gaspar")
    myH.show(myH.root)
   

if __name__ == "__main__":
    main() 
    print("Adios") 
    os.system("pause")
    