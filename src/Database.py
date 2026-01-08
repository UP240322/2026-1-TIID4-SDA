class Database:
    def __init__(self):
        self.datos = []
    
    def agregar(self, item):
        self.datos.append(item)
        print(f"Item agregado: {item}")
    
    def obtener_todos(self):
        return self.datos

    