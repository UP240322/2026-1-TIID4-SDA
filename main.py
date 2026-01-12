# main.py

# 1. Importaciones estándar de Python
import os
import sys
import subprocess

# 2. Importaciones de terceros
import requests
import numpy as np

# 3. Importaciones locales (tus propios módulos)
from src.calculadora import sumar, restar  # importar funciones específicas
import src.calculadora as calc             # importar todo el módulo
from src.Database import Database

# 4. Funciones auxiliares
def configurar_programa():
    """Configuración inicial del programa"""
    print("Configurando el programa...")
    # Tu código aquí

def ejecutar_tarea_principal():
    """Lógica principal del programa"""
    print("Ejecutando tarea principal...")
    resultado = calc.sumar(5, 3)
    print(f"Resultado: {resultado}")

def main():  
    db = Database()
    db.agregar("Elemento 1")
    db.agregar("Elemento 2")
    obtener = db.obtener_todos()
    print(f"Elementos en la base de datos: {obtener}")
    for dato in obtener:
            print(f"  - {dato}")  

# 5. Punto de entrada principal
if __name__ == "__main__":
    print("Iniciando programa...")
    configurar_programa()
    ejecutar_tarea_principal()
    main()
    print("Programa finalizado.")
    
    resultado = subprocess.run(
        ["python", "src/calculadora.py"],
        capture_output=True,
        text=True
    )
    print(resultado.stdout)
    main()
